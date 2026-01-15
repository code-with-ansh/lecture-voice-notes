print("[BOOT] transcriber.py loaded")

import whisper
import os

def transcribe(audio_path: str):
    print("[INFO] transcribe() called")
    print(f"[INFO] Audio path: {audio_path}")
    print(f"[INFO] File exists: {os.path.exists(audio_path)}")

    model = whisper.load_model("base")
    print("[INFO] Model loaded")

    result = model.transcribe(audio_path)
    return result["text"]


if __name__ == "__main__":
    print("[MAIN] __main__ block entered")

    audio_file = "backend/data/audio/sample.wav"

    print("[MAIN] Starting transcription...")
    text = transcribe(audio_file)

    print("\n--- FINAL TRANSCRIPTION ---\n")
    print(text)
