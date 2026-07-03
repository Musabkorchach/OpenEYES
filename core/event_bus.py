class EventBus:
    """
    OpenEyes Event Bus
    Allows different modules to communicate without direct dependencies.
    """

    def __init__(self):
        self._listeners = {}

    def subscribe(self, event_name, callback):
        """Register a callback for an event."""
        if event_name not in self._listeners:
            self._listeners[event_name] = []

        self._listeners[event_name].append(callback)

    def publish(self, event_name, data=None):
        """Send an event to all registered listeners."""
        if event_name not in self._listeners:
            return

        for callback in self._listeners[event_name]:
            callback(data)

    def unsubscribe(self, event_name, callback):
        """Remove a callback."""
        if event_name not in self._listeners:
            return

        if callback in self._listeners[event_name]:
            self._listeners[event_name].remove(callback)

    def clear(self):
        """Remove all listeners."""
        self._listeners.clear()