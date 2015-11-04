# encoding: utf-8

from django.db import models


class Movement(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(choices=(('credit', 'Crédit'), ('debit', 'Débit')), max_length=6)

    comment = models.TextField(null=True, blank=True)
