from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class GroqClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        model = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

        if not api_key:
            raise ValueError("❌ Falta GROQ_API_KEY en .env")

        self.client = Groq(api_key=api_key)
        self.model = model

    def chat(self, system_prompt, user_message):
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            model=self.model,
            temperature=0.7,
            max_completion_tokens=512
        )

        return response.choices[0].message.content