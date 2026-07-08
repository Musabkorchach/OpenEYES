from kernel.event_bus import EventBus
from kernel.logger import KernelLogger
from kernel.scheduler import KernelScheduler


class OpenEyesRuntime:
    def __init__(self):
        self.logger = KernelLogger()
        self.event_bus = EventBus()
        self.scheduler = KernelScheduler()
        self.running = False

    def boot(self):
        self.logger.info("OpenEyes Runtime booting...")
        self.event_bus.publish("runtime_booting")
        self.running = True
        self.logger.info("OpenEyes Runtime ready.")

    def shutdown(self):
        self.logger.info("OpenEyes Runtime shutting down...")
        self.event_bus.publish("runtime_shutdown")
        self.running = False
        self.logger.info("OpenEyes Runtime stopped.")

    def status(self):
        return {
            "running": self.running,
            "event_bus": "ready",
            "scheduler": "ready",
            "logger": "ready",
        }