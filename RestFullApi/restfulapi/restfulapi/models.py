from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # this is for showing name of Drink objects in the admin panel instead of Drink object(1)
    def __str__(self):
        return self.name
