import openai
import os
CHATGPT_KEY = os.getenv("OPENAI_API_KEY")

class GPT_search:
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=CHATGPT_KEY
        )
    
    def search(self, input):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": input}]
        )
        return completion.choices[0].message.content

