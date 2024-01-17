from django.db import models

class Template(models.Model):
    course_name = models.TextField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.title