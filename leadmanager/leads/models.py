from django.db import models
from django.utils.text import slugify


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    lead_objects = models.Manager()

    def __str__(self):
        return self.name


# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(GeeksModel, self).save(*args, **kwargs)
