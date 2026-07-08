import time


class KernelScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, callback, interval):
        self.tasks.append({
            "name": name,
            "callback": callback,
            "interval": interval,
            "last_run": 0
        })

    def update(self):
        now = time.time()

        for task in self.tasks:
            if now - task["last_run"] >= task["interval"]:
                task["callback"]()
                task["last_run"] = now