# backend/api.py

from backend.stt.transcriber import transcribe
from backend.nlp.summarizer import LectureSummarizer
from backend.nlp.quiz_generator import QuizGenerator
from backend.nlp.flashcard_generator import FlashcardGenerator

# Initialize models once (important for performance)
_summarizer = LectureSummarizer()
_quiz_generator = QuizGenerator()
_flashcard_generator = FlashcardGenerator()


def run_transcription(audio_path: str) -> str:
    """
    Speech → Text
    """
    return transcribe(audio_path)


def run_summary(transcript: str) -> str:
    """
    Transcript → Study Notes
    """
    return _summarizer.summarize(transcript)


def run_quiz(transcript: str):
    """
    Transcript → MCQ Quiz
    """
    return _quiz_generator.generate_quiz(transcript)


def run_flashcards(transcript: str):
    """
    Transcript → Flashcards
    """
    return _flashcard_generator.generate_flashcards(transcript)
