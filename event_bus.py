class EventBus:
    """
    A simple event bus implementation that allows subscribing to and publishing events.
    """

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, system):
        """
        Subscribe a system to a specific event type.

        Args:
            event_type (str): The type of event to subscribe to.
            system (object): The system object that will handle the event.
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(system)

    def publish(self, event):
        """
        Publish an event to all subscribed systems.

        Args:
            event (object): The event object to publish.
        """
        for system in self.subscribers.get(event.type, []):
            system.handle_event(event)