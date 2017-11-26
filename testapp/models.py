# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djangotoolbox.fields import ListField


class Post(models.Model):
    title = models.CharField(max_length = 50)
    text = models.TextField()
    tags = ListField()
    comments = ListField()

# Create your models here.
