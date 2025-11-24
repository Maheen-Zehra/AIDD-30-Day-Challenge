SUMMARIZE_PROMPT_TEMPLATE = """
You are an expert at summarizing technical documents. Your task is to provide a clean, concise, and meaningful summary of the following text.
The summary should capture the key concepts, main arguments, and any significant conclusions.
Do not include any introductory or concluding phrases like "Here is a summary of the text:".

Text to summarize:
---
{text}
---
"""

QUIZ_PROMPT_TEMPLATE = """
You are an expert quiz creator. Based on the text provided below, generate a multiple-choice quiz with 5 questions.
The quiz should cover the main topics and key details from the text.

For each question, provide:
- The question itself.
- 4 possible answers (A, B, C, D).
- The correct answer.

Return the quiz as a valid JSON object. The JSON object should be a list of dictionaries, where each dictionary represents a single question and has the following keys: "question", "options" (a dictionary of A, B, C, D), and "answer" (the key of the correct option, e.g., "A").

Do not include any text outside of the JSON object itself.

Example format:
[
  {{
    "question": "What is the capital of France?",
    "options": {{
      "A": "London",
      "B": "Berlin",
      "C": "Paris",
      "D": "Madrid"
    }},
    "answer": "C"
  }}
]

Text to use for the quiz:
---
{text}
---
"""
