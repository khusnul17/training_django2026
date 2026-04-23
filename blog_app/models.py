from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_by = models.CharField(max_length=225)
    created_at = models.DateTimeField()
    modified_by = models.CharField(max_length=225)
    modified_at = models.DateTimeField()
