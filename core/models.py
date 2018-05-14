# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date


def save_file(instance, filename):
    ext = filename.split('.')[-1]

    if ext.lower() in ['gif', 'jpg', 'jpeg', 'png']:
        folder = "pictures/"
    else:
        folder = "video/"
        
    path = ''.join([date.today().strftime(
        'uploads/%Y/%m/%d/'), folder, filename])

    return path


class MediaFile(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to=save_file)
    uploaded_at = models.DateTimeField(auto_now_add=True)
