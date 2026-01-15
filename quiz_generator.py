import random
import re
from transformers import pipeline


class QuizGenerator:
    def __init__(self):
        self.extractor = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            device=-1
        )

    def _extract_facts(self, text: str):
        prompt = f"""
        Extract 5 factual statements strictly from the text below.
        Do NOT add new information.
        Each fact should be one sentence.

        Text:
        {text}
        """

        output = self.extractor(
            prompt,
            max_length=256,
            do_sample=False
        )[0]["generated_text"]

        facts = [
            f.strip("-• ").strip()
            for f in output.split("\n")
            if len(f.strip()) > 30
        ]

        return facts[:5]

    def _build_question(self, fact: str):
        return f"What does the following statement describe?\n\n{fact}"

    def _build_distractors(self, correct: str):
        words = re.findall(r"\b[A-Za-z]{5,}\b", correct)

        distractors = []
        for w in words:
            distractors.append(f"A concept related to {w}")

        while len(distractors) < 3:
            distractors.append("An unrelated concept")

        return list(set(distractors))[:3]

    def generate_quiz(self, text: str):
        quiz = []
        facts = self._extract_facts(text)

        for fact in facts:
            question = self._build_question(fact)
            correct = fact

            distractors = self._build_distractors(correct)
            options = distractors + [correct]
            random.shuffle(options)

            quiz.append({
                "question": question,
                "options": options,
                "answer": correct
            })

        return quiz
