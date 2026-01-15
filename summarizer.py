from transformers import pipeline

class LectureSummarizer:
    def __init__(self):
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1  # CPU
        )

    def summarize(self, text: str) -> str:
        if len(text.strip()) == 0:
            return ""

        # Chunk long transcripts safely
        max_chunk = 900
        chunks = [text[i:i + max_chunk] for i in range(0, len(text), max_chunk)]

        summaries = []
        for chunk in chunks:
            summary = self.summarizer(
                chunk,
                max_length=150,
                min_length=60,
                do_sample=False
            )[0]["summary_text"]
            summaries.append(summary)

        return "\n\n".join(summaries)
