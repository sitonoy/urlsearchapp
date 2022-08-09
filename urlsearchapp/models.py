from django.db import models
from datetime import date
from django.utils import timezone


class Searchlist(models.Model):
    result = models.CharField(max_length=200, blank=True, null=True)
    URL = models.CharField(max_length=200, blank=True, null=True)
    registered_date = models.DateField(default=timezone.now)
    proba = models.FloatField(default=0.0)


def __str__(self):
    if self.proba == 0.0:
        return '%s' % (self.registered_date.strftime('%Y-%m-%d'))
    else:
        return '%s, %d' % (self.registered_date.strftime('%Y-%m-%d'), self.proba)
