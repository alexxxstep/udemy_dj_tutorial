from django.db import models


# Create your models here.
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.isbn_10


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

    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='characters')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=True, default='')
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return ' '.join([self.name, self.surname])
