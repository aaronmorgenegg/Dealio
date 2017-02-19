from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Promotion(models.Model):
    title = models.CharField(max_length=25, unique=True)  # specify the models fields (data type) based on what django provides
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title


class Restaurant(models.Model):
    name = models.CharField(max_length=25, unique=True)
    proms = models.ManyToManyField(Promotion)
    review_link = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_review_link(self):
        return self.review_link

    def getPromotions(self):
        promos = []
        for i in range(0,self.proms.count()):
            promos.append(self.proms.all()[i])
        return promos