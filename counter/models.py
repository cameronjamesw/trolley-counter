from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Status(models.IntegerChoices):
    EIGHT = 1, 'Eight Totes'
    TEN = 2, 'Ten Totes'

class Shapes(models.IntegerChoices):
    SQUARE = 1, 'Square'
    CIRCLE = 2, 'Circle'
    TRIANGLE = 3, 'Triangle'
    CROSS = 4, 'Cross'
    SQUIGGLE = 5, 'Squiggle'
    HEART = 6, 'Heart'
    FLOWER = 7, 'Flower'
    PENGUIN = 8, 'Penguin'
    BOWTIE = 9, 'Bowtie'
    AIRPLANE = 10, 'Airplane'

class Trolley(models.Model):
    id = models.AutoField(primary_key=True)
    totes_count = models.IntegerField(choices=Status.choices, default=Status.EIGHT)
    date_added = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=200)

    def __str__(self):
        return f"Trolley number {self.id}"

class Shape(models.Model):
    trolley = models.ForeignKey(Trolley, on_delete=models.CASCADE)
    shape = models.IntegerField(choices=Shapes.choices, default=Shapes.SQUARE)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"A {self.shape} tote, linked to trolley number: {self.trolley.id}"

    def save(self, *args, **kwargs):
        if self.trolley and not self.pk:  # Only enforce on create
            if self.trolley.totes_count == 1 & Shape.objects.filter(trolley=self.trolley).count() >= 8:
                raise ValidationError("Small trolley's cannot have more than 8 totes!.")
            elif self.trolley.totes_count == 1 & Shape.objects.filter(trolley=self.trolley).count() >= 10:
                raise ValidationError("Big trolley's cannot have more than 10 totes!.")
        super().save(*args, **kwargs)