"""
OpenEyes Core Engine
"""

from core.startup import startup
from core.shutdown import shutdown


class OpenEyesEngine:
    def __init__(self):
        self.running = False

    def start(self):
        startup()
        self.running = True
        print("OpenEyes is ready.")
        print("Type 'status' or 'exit'.")

        while self.running:
            command = input("OpenEyes > ").strip().lower()

            if command == "status":
                print("Status: running")

            elif command in ["exit", "quit", "stop"]:
                self.stop()

            else:
                print("Unknown command.")

    def stop(self):
        self.running = False
        shutdown()