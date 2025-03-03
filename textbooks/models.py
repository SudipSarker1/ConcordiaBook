from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    edition = models.CharField(max_length=50, blank=True, null=True)
    course_code = models.CharField(max_length=20)
    condition = models.CharField(max_length=50, blank=True, null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"

