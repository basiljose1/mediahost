# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from core.forms import MediaFileForm
from core.models import MediaFile


class MediaUploadView(View):
    def get(self, request):
        media_list = MediaFile.objects.all()
        return render(self.request, 'upload.html', {'medias': media_list})

    def post(self, request):
        form = MediaFileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name,
                    'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
