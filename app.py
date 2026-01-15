# frontend/app.py

import sys
from pathlib import Path
import tempfile

import streamlit as st
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# -------------------------------------------------
# Fix backend import path
# -------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from backend.api import (
    run_transcription,
    run_summary,
    run_quiz,
    run_flashcards,
)

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Lecture Voice-to-Notes Generator",
    layout="wide",
)

# -------------------------------------------------
# Session State Initialization
# -------------------------------------------------
for key in [
    "audio_path",
    "transcript",
    "notes",
    "quiz",
    "flashcards",
]:
    if key not in st.session_state:
        st.session_state[key] = None

# -------------------------------------------------
# Audio Recording Utility
# -------------------------------------------------
def record_audio(duration: int = 30, sample_rate: int = 16000) -> str:
    st.info(f"🎙️ Recording for {duration} seconds...")
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype=np.int16,
    )
    sd.wait()

    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_wav.name, sample_rate, recording)

    return temp_wav.name

# -------------------------------------------------
# Sidebar — Audio Input
# -------------------------------------------------
st.sidebar.title("🎙️ Audio Input")

input_mode = st.sidebar.radio(
    "Choose input method:",
    ["Upload Audio", "Record Live"],
)

if input_mode == "Upload Audio":
    uploaded_file = st.sidebar.file_uploader(
        "Upload lecture audio (.wav)",
        type=["wav"],
    )
else:
    uploaded_file = None
    duration = st.sidebar.slider(
        "Recording duration (seconds)",
        min_value=10,
        max_value=120,
        value=30,
        step=10,
    )

    if st.sidebar.button("🎤 Start Recording"):
        st.session_state.audio_path = record_audio(duration)
        st.success("Recording completed ✔")

# -------------------------------------------------
# Main UI
# -------------------------------------------------
st.title("🎙️ Lecture Voice-to-Notes Generator")

st.markdown(
    """
Convert lecture audio into:
- 📝 Transcript  
- 📘 Study Notes  
- ❓ Quiz  
- 🧠 Flashcards  
"""
)

# -------------------------------------------------
# Handle Uploaded Audio
# -------------------------------------------------
if uploaded_file:
    audio_path = "backend/data/audio/sample.wav"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())
    st.session_state.audio_path = audio_path

# -------------------------------------------------
# Step 1 — Transcription
# -------------------------------------------------
if st.session_state.audio_path and st.button("🔊 Transcribe Audio"):
    st.session_state.transcript = run_transcription(
        st.session_state.audio_path
    )

    # Reset downstream outputs
    st.session_state.notes = None
    st.session_state.quiz = None
    st.session_state.flashcards = None

# -------------------------------------------------
# Transcript View
# -------------------------------------------------
if st.session_state.transcript:
    st.subheader("📝 Transcript")
    st.text_area(
        "Transcript",
        st.session_state.transcript,
        height=220,
    )

# -------------------------------------------------
# Step 2 — Study Notes
# -------------------------------------------------
if st.session_state.transcript and st.button("📘 Generate Study Notes"):
    st.session_state.notes = run_summary(st.session_state.transcript)

if st.session_state.notes:
    st.subheader("📘 Study Notes")
    st.text_area(
        "Notes",
        st.session_state.notes,
        height=220,
    )

# -------------------------------------------------
# Step 3 — Quiz
# -------------------------------------------------
if st.session_state.transcript and st.button("❓ Generate Quiz"):
    st.session_state.quiz = run_quiz(st.session_state.transcript)

if st.session_state.quiz:
    st.subheader("❓ Quiz")
    for i, q in enumerate(st.session_state.quiz, start=1):
        st.markdown(f"**Q{i}. {q['question']}**")
        for opt in q["options"]:
            st.write(f"- {opt}")
        st.markdown(f"✅ **Answer:** {q['answer']}")
        st.divider()

# -------------------------------------------------
# Step 4 — Flashcards (FIXED DATA FLOW)
# -------------------------------------------------
st.subheader("🧠 Flashcards")

if not st.session_state.notes:
    st.info("Generate study notes before creating flashcards.")
else:
    if st.button("🧠 Generate Flashcards"):
        st.session_state.flashcards = run_flashcards(
            st.session_state.notes   # ✅ CORRECT INPUT
        )

    if st.session_state.flashcards:
        cols = st.columns(2)
        for i, card in enumerate(st.session_state.flashcards):
            with cols[i % 2]:
                with st.container(border=True):
                    st.markdown(f"**📌 {card['question']}**")
                    st.markdown(card["answer"])
