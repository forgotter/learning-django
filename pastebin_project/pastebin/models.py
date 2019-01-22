from django.db import models

class Note(models.Model):
    title = models.CharField(max_length = 50)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_id(self):
        return id
