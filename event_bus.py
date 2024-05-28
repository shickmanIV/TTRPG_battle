class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, system):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(system)

    def publish(self, event):
        for system in self.subscribers.get(event.type, []):
            system.handle_event(event)