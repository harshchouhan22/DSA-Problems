import json

class LogMixin:
    def log(self, message):
        print(f"Log message is: {message} ")

class JSONdata:
    def to_json(self):
        result =  json.dumps(self.__dict__)
        return result

class Person(LogMixin, JSONdata):
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Harsh', 21)

person.log("Calling log")
result = person.to_json()
print(result)


