

class Event:
    def __init__(self, name):
        self.name = name
        self.handlers = []

    def connect(self, handler):
        self.handlers.append(handler)
    
    def disconnect(self, handler):
        if handler in self.handlers:
            self.handlers.remove(handler)
        else:
            print(f"Handler {handler} not found in the list of handlers.")

    def fire(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)

def handler1(arg):
    print(f"Handler 1: {arg}")

def handler2(arg):
    print(f"Handler 2: {arg}")


my_event = Event("my_event")
my_event.connect(handler1)
my_event.connect(handler2)

my_event.fire("Event is happening!")


