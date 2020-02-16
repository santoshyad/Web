from django.db import models


class business(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    features = models.TextField()
    price = models.FloatField()


class Jobapply(models.Model):
    fn = models.CharField(max_length=100, default="")
    ln = models.CharField(max_length=100, default="")
    un = models.CharField(max_length=100, default="")
    ci = models.CharField(max_length=100, default="")
    zi = models.FloatField()

