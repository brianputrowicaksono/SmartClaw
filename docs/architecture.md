import os
from dotenv import load_dotenv

load_dotenv()

class SmartClaw:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.tools = ["web_search", "calculator"]
        print(f"SmartClaw Agent siap dengan model {self.model}")

    def plan(self, task):
        print(f"Membuat rencana untuk: {task}")
        return ["Search info", "Analyze data", "Provide summary"]

    def execute(self, plan):
        for step in plan:
            print(f"Mengeksekusi: {step}...")
        return "Selesai!"

if __name__ == "__main__":
    claw = SmartClaw()
    rencana = claw.plan("Cari harga saham terbaru")
    claw.execute(rencana)
