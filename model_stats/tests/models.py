# -*- coding: utf-8 -*-


from django.db import models


class Model(models.Model):
    name = models.CharField(default='some model')
    views = models.IntegerField(default=0)
