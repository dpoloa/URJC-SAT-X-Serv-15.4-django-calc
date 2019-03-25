from django.db import models


class Calculadora(models.Model):
    operation = models.CharField(max_length=10)
    operator = models.IntegerField()
