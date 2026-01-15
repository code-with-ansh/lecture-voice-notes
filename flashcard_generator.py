from transformers import pipeline


class FlashcardGenerator:
    def __init__(self):
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            device=-1
        )

    def generate_flashcards(self, notes: str):
        prompt = f"""
        Create 5 study flashcards from the notes below.

        Rules:
        - Question and Answer format
        - Concept-focused
        - Short answers (2–3 sentences)
        - No multiple choice
        - No numbering

        Notes:
        {notes}

        Example:
        Q: What is Artificial Intelligence?
        A: Artificial Intelligence is the simulation of human intelligence in machines.
        """

        output = self.generator(
            prompt,
            max_length=512,
            do_sample=False
        )[0]["generated_text"]

        flashcards = []
        current_q = None

        for line in output.split("\n"):
            line = line.strip()

            if line.lower().startswith("q"):
                current_q = line.split(":", 1)[-1].strip()

            elif line.lower().startswith("a") and current_q:
                answer = line.split(":", 1)[-1].strip()
                flashcards.append({
                    "question": current_q,
                    "answer": answer
                })
                current_q = None

        # 🔒 HARD FALLBACK (never empty)
        if not flashcards:
            flashcards.append({
                "question": "Explain the main concept discussed in the lecture.",
                "answer": notes[:300] + "..."
            })

        return flashcards
