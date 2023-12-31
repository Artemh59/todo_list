from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(default="none")
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.content
