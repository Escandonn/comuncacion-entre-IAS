from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class GroqClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        model = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "256"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))

        if not api_key:
            raise ValueError("Falta GROQ_API_KEY en .env")

        self.client = Groq(api_key=api_key)
        self.model = model

    def chat(self, system_prompt: str, user_message: str, max_tokens: int = 0, temperature: float = 0.0) -> str:
        try:
            max_tokens = max_tokens or self.max_tokens
            temperature = temperature or self.temperature

            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                model=self.model,
                temperature=temperature,
                max_completion_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()
        except Exception as error:
            raise RuntimeError(f"Error en la API de Groq: {error}")
