from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=100)
    PRESENCE_CHOICES = [
        ('yes', 'да'),
        ('no', 'нет'),
    ]
    presence = models.CharField(max_length=3, choices=PRESENCE_CHOICES, blank=True, null=True)
    PLUS_ONE_CHOICES = [
        ('yes', 'да'),
        ('no', 'нет'),
    ]
    plusone = models.CharField(max_length=3, choices=PLUS_ONE_CHOICES, blank=True, null=True)

    drink = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
