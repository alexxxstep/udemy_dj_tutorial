from django.db import models


# Create your models here.

class Book(models.Model):
    BOOKS = (('HB', 'Hobbit',),
             ('LOTR', 'Lord of the ring'))

    STATUSES = (
        (0, 'Unknown'),
        (1, 'processed'),
        (2, 'paid')
    )

    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=265, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True, default='')
    author = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=150, blank=False)
