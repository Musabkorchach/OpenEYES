from datetime import datetime
from pathlib import Path


class KernelLogger:
    def __init__(self, log_file="logs/openeyes.log"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def info(self, message):
        self._write("INFO", message)

    def warning(self, message):
        self._write("WARNING", message)

    def error(self, message):
        self._write("ERROR", message)

    def _write(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] [{level}] {message}"

        print(line)

        with self.log_file.open("a", encoding="utf-8") as file:
            file.write(line + "\n")