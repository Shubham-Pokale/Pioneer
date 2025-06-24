import time
from base_agent import BaseAgent

class PongerAgent(BaseAgent):
    def run(self):
        """Listen for messages and respond to pings."""
        print(f"Ponger agent '{self.name}' starting. Listening for messages...")
        while True:
            messages = self.get_messages()
            for msg in messages:
                sender = msg.get('sender')
                content = msg.get('content')
                print(f"Received: '{content}' from '{sender}'")
                if content == "ping":
                    print("Responding with: pong")
                    self.send_message(sender, "pong")
            time.sleep(2) # Poll for messages every 2 seconds

if __name__ == "__main__":
    ponger = PongerAgent(name="ponger-agent")
    ponger.run() 