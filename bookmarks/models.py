from django.db import models

# Create models here
class Bookmark(models.Model):
  id = models.UUIDField(primary_key=True, defualt=uuid4, editable=False)
  url = models.URLField('URL', unique=True)
  name = models.CharField(max_length=200)
  notes = models.TextField(blank=True)