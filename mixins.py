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

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#mixins.py

class TimstampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True

#models.py
class Post(TimstampMixin, models.Model):
    title = models.CharField(max_length = 255)
    content  = models.TextField()


from django.utils.text import slugify

class SlugMixin(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length = 255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)




