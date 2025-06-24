import time
from base_agent import BaseAgent

class PingerAgent(BaseAgent):
    def __init__(self, name, ponger_name="ponger-agent"):
        super().__init__(name)
        self.ponger_name = ponger_name

    def run(self):
        """Periodically send a 'ping' message."""
        print(f"Pinger agent '{self.name}' starting. Will send pings to '{self.ponger_name}'.")
        while True:
            print("Sending: ping")
            self.send_message(self.ponger_name, "ping")
            time.sleep(5)

if __name__ == "__main__":
    pinger = PingerAgent(name="pinger-agent")
    pinger.run() 