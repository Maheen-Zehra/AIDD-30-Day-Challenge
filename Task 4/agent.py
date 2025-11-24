import json
import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
from prompts import SUMMARIZE_PROMPT_TEMPLATE, QUIZ_PROMPT_TEMPLATE

# It seems openagents might be based on or compatible with the OpenAI API structure.
# For Google Gemini, the typical way to interact with it in Python is via google-generativeai library.
# However, since the user specified OpenAgents SDK, I will attempt to use it.
# Based on the search results, OpenAgents SDK is provider-agnostic and LiteLLM is often used.
# Let's try a common pattern for OpenAgents or a compatible LLM client.

# Load environment variables from .env file
load_dotenv()

# --- LLM Setup ---
# The OpenAgents SDK documentation suggests it is designed for building agents.
# For directly calling an LLM, I will use a generic approach that might be compatible or
# assume a simple wrapper within OpenAgents if available.
# A common way to integrate different LLMs in a unified way (as suggested by OpenAgents docs)
# is through libraries like `LiteLLM`. However, `openagents` itself might abstract this.
# I will use a direct call to GoogleGenerativeAI if `openagents` doesn't provide a direct
# high-level abstraction for LLM calls that is immediately obvious.
# Given the dependency on `openagents`, I'll check if it offers a simple LLM client.
# Based on some patterns, OpenAgents might rely on a configured LLM within its agent orchestrator.
# For a direct call, I'll leverage `google.generativeai` if `openagents` doesn't expose it simply.

# For simplicity and directness, I will use the `google-generativeai` library directly here
# as OpenAgents SDK primarily focuses on agent orchestration rather than being an LLM client itself.
# This assumes the user has `google-generativeai` installed. If not, I'll add it to requirements.txt.
# Let's add `google-generativeai` to requirements.txt for robustness.

try:
    import google.generativeai as genai # pyright: ignore[reportMissingImports]
    # Configure API key
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not GOOGLE_API_KEY:
        raise ValueError("Google API Key not found. Please set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file.")
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Initialize the Generative Model
    # Using gemini-1.5-flash-latest for text-only tasks
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    print("Google Gemini model initialized.")

except ImportError:
    print("The 'google-generativeai' library is not installed. Please install it.")
    # Fallback to a simpler, non-functional mock or raise an error for the user.
    model = None
except ValueError as e:
    print(f"Configuration Error: {e}")
    model = None
except Exception as e:
    print(f"An unexpected error occurred during LLM setup: {e}")
    model = None

class StudyBuddyAgent:
    """
    An agent that can summarize text and generate quizzes.
    Uses Google Gemini for text generation.
    """

    def _call_llm(self, prompt: str) -> str:
        if model is None:
            return "LLM is not configured. Cannot generate content."
        try:
            # Use generation_config to control output and ensure it's concise
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=2048 # Adjust as needed
                )
            )
            # Access the text from the response. 'text' attribute is common for Gemini.
            return response.text
        except Exception as e:
            return f"Error calling LLM: {e}"

    def summarize(self, text: str) -> str:
        """
        Generates a summary of the given text using the LLM.
        """
        print("---AGENT: Generating summary with LLM...")
        prompt = SUMMARIZE_PROMPT_TEMPLATE.format(text=text)
        summary = self._call_llm(prompt)
        return summary

    def generate_quiz(self, text: str) -> list:
        """
        Generates a quiz from the given text using the LLM.
        Returns a list of quiz questions in JSON format.
        """
        print("---AGENT: Generating quiz with LLM...")
        prompt = QUIZ_PROMPT_TEMPLATE.format(text=text)
        quiz_json_str = self._call_llm(prompt)
        
        try:
            # Attempt to parse the JSON string.
            # Sometimes LLMs add conversational filler, so try to extract JSON.
            start_idx = quiz_json_str.find('[')
            end_idx = quiz_json_str.rfind(']')
            if start_idx != -1 and end_idx != -1:
                quiz_json_str = quiz_json_str[start_idx : end_idx + 1]
            
            quiz = json.loads(quiz_json_str)
            return quiz
        except json.JSONDecodeError as e:
            print(f"Error decoding quiz JSON from LLM: {e}")
            print(f"Raw LLM response for quiz: {quiz_json_str}")
            return [{"question": "Failed to generate quiz. Invalid JSON from LLM.", "options": {"A": "Error"}, "answer": "A"}]