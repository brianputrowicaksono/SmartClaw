import os
from dotenv import load_dotenv

# Memuat kunci API dari file .env
load_dotenv()

class SmartClaw:
    def __init__(self):
        self.name = "SmartClaw"
        print(f"{self.name} Agent Initialized!")

    def run(self, task):
        print(f"Sedang mengerjakan tugas: {task}")
        # Logika AI akan masuk di sini nanti
        return "Tugas selesai dikerjakan oleh SmartClaw."

if __name__ == "__main__":
    agent = SmartClaw()
    hasil = agent.run("Sapa dunia!")
    print(hasil)
