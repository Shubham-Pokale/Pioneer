import requests
import time

class BaseAgent:
    def __init__(self, name, server_url="http://127.0.0.1:8000"):
        self.name = name
        self.server_url = server_url
        self.register()

    def register(self):
        """Register the agent with the MCP server."""
        try:
            response = requests.post(f"{self.server_url}/register", json={"name": self.name})
            if response.status_code == 200:
                print(f"Agent '{self.name}' registered successfully.")
            elif response.status_code == 400 and "already registered" in response.json().get("detail", ""):
                print(f"Agent '{self.name}' was already registered.")
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error registering agent: {e}")
            exit()

    def send_message(self, recipient, content):
        """Send a message to another agent."""
        try:
            response = requests.post(
                f"{self.server_url}/send",
                json={"sender": self.name, "recipient": recipient, "content": content}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {e}")
            return None

    def get_messages(self):
        """Retrieve new messages from the server."""
        try:
            response = requests.get(f"{self.server_url}/messages/{self.name}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving messages: {e}")
            return []

    def run(self):
        """The main loop of the agent. To be implemented by subclasses."""
        raise NotImplementedError("Each agent must implement its own run loop.") 