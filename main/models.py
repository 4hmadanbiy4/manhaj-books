from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()

BOOK_CHOICES = [
    ('Fathul Qorib', 'Fathul Qorib'),
    ("I'anatut tholibin", "I'anatut tholibin"),
    ("Is'adur rofiq", "Is'adur rofiq"),
    ("Siroh nabawiyah", "Siroh nabawiyah"),
    ("Shohih bukhori", "Shohih bukhori"),
    ("Shohih muslim", "Shohih muslim"),
    ("Idhohul mubham", "Idhohul mubham")
]

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pemesan = models.CharField(max_length=100)
    buku = models.CharField(max_length=100, choices=BOOK_CHOICES)
    pcs = models.IntegerField()

    def __str__(self):
        return f"{self.pemesan} - {self.buku}"