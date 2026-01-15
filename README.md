# Lecture Voice-to-Notes Generator

An AI-powered application that converts recorded or live lecture audio into structured study material including transcripts, summarized notes, quizzes, and flashcards.

This project helps students overcome the difficulty of listening and taking notes simultaneously by automating the note-generation process using modern speech-to-text and NLP models.

---------------------------------------------------------------------------------

# Features

Speech-to-Text Transcription  
Converts lecture audio (`.wav`) into accurate text using Whisper-based models.

Live Voice Recording  
Allows users to record lecture audio directly using the system microphone without uploading files.

Study Notes Generation  
Summarizes long lecture transcripts into concise, readable notes.

Quiz Generation  
Automatically generates multiple-choice questions (MCQs) from lecture content.

Flashcards  
Creates question–answer style flashcards for quick revision.

Simple Web Interface  
Built using Streamlit for quick interaction and demonstration.

---------------------------------------------------------------------------------

# Tech Stack

# Backend  
Python  
Whisper / Faster-Whisper – Speech-to-text  
Hugging Face Transformers  
  BART – Text summarization  
  T5-based models – Quiz & flashcard generation  
PyTorch  

# Frontend  
Streamlit  

# Utilities  
NumPy, Pandas  
SoundDevice, SciPy – Live audio recording  
Python-dotenv  
FFmpeg (for audio handling)

---------------------------------------------------------------------------------

# Project Structure

lecture-voice-notes/  
│  
├── backend/  
│   ├── api.py  
│   ├── stt/  
│   │   └── transcriber.py  
│   ├── nlp/  
│   │   ├── summarizer.py  
│   │   ├── quiz_generator.py  
│   │   └── flashcard_generator.py  
│   └── data/  
│       └── audio/  
│  
├── frontend/  
│   └── app.py  
│  
├── venv/  
├── requirements.txt  
└── README.md  

---------------------------------------------------------------------------------

# Installation & Setup

1. Clone the repository  

powershell:  
git clone <repository-url>

2. Navigate to the project directory  
cd lecture-voice-notes  

3. Set up a virtual environment  
python -m venv venv  

4. Activate the virtual environment  
venv\Scripts\activate  

5. Install dependencies  
pip install -r requirements.txt  

6. Start the application  
streamlit run frontend/app.py  

The application will be available at:  
http://localhost:8501  

---------------------------------------------------------------------------------

# Application Workflow

Choose audio input method:
- Upload a lecture audio file (`.wav`)  
- OR record live audio using the microphone  

Click Transcribe Audio 
View the generated transcript  
Generate:
- Study Notes  
- Quiz  
- Flashcards  

All outputs are generated from the same lecture content.

---------------------------------------------------------------------------------

# Live Voice Recording

The application supports live microphone recording in addition to audio file uploads.

How it works:
- Audio is recorded locally using the system microphone.
- Recording is handled using `sounddevice` and saved as a temporary `.wav` file.
- The recorded audio follows the same processing pipeline as uploaded audio.

Why this approach:
- Streamlit does not natively support real-time browser audio streaming.
- A Python-based recording approach ensures stability, cross-platform support, and reliability.
- Designed as a record → stop → process workflow, ideal for lecture capture.

Limitations:
- Recording duration is capped (demo-safe configuration).
- Real-time transcription is not supported.

---------------------------------------------------------------------------------

# Design Decisions

Modular backend architecture for easy extensibility  
Separate NLP components for summarization, quiz, and flashcards  
Deterministic generation for reliability and demo stability  
Session state used to maintain UI consistency  
Streamlit chosen for rapid prototyping and demonstration  
Focused on core AI functionality rather than UI complexity  

---------------------------------------------------------------------------------

# Limitations & Future Improvements (Very IMP)

Quiz and flashcard quality can be improved using larger instruction-tuned LLMs (e.g., Meta-LLaMA)  
UI can be enhanced using a React-based frontend  
Support for more audio formats  
Longer-duration live recording  
PDF export of notes and quizzes  

These enhancements were intentionally deferred to prioritize system stability and timely submission.

---------------------------------------------------------------------------------

# Use Case

Students attending recorded or live lectures  
Revision and exam preparation  
Automated study material generation  
AI-powered educational tools  

---------------------------------------------------------------------------------

# Developer

Ansh Rathi  
Internship Project – AI / Machine Learning  

---------------------------------------------------------------------------------
