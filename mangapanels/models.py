import datetime
import uuid

from django.db import models
from django.utils import timezone

class Manga(models.Model):
    """
    Manga is effectively a book written by an author, and published sometimes
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.DateField()

    def __str__(self) -> str:
        return f'Title: {self.title}, Author: {self.author}, Published: {self.published}'

    def is_published_recently(self) -> bool:
        return self.published >= timezone.now() - datetime.timedelta(days=1)
