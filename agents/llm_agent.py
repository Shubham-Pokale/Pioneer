import os
import time
import requests
from base_agent import BaseAgent

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://router.huggingface.co/fireworks-ai/inference/v1/chat/completions"
MODEL = "accounts/fireworks/models/deepseek-r1-0528"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
}

def query_huggingface(message_content):
    if not HF_TOKEN:
        print("Error: HF_TOKEN environment variable not set.")
        return "[Error: No API key configured]"
    payload = {
        "messages": [
            {"role": "user", "content": message_content}
        ],
        "model": MODEL
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        # Extract the assistant's reply
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Exception: {e}]"

class LLMAgent(BaseAgent):
    def run(self):
        print(f"LLM agent '{self.name}' starting. Listening for messages...")
        while True:
            messages = self.get_messages()
            for msg in messages:
                sender = msg.get('sender')
                content = msg.get('content')
                print(f"Received from '{sender}': {content}")
                response = query_huggingface(content)
                print(f"Replying to '{sender}': {response}")
                self.send_message(sender, response)
            time.sleep(2)

if __name__ == "__main__":
    agent = LLMAgent(name="llm-agent")
    agent.run() 