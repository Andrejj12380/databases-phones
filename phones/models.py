from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 40)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)