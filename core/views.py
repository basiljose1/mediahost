# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from filebrowser.sites import site
from filebrowser.base import FileListing

from core.forms import MediaFileForm
from core.models import MediaFile

import os


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


class MediaHierarchyView(View):
    def get(self, request):
        query = request.GET.copy()
        path = u'%s' % os.path.join(
            site.storage.location, 'uploads/', query.get('dir', ''))
        filelisting = FileListing(
            path, sorting_by='date', sorting_order='desc')
        listing = filelisting.files_listing_filtered()
        files = []
        for fileobject in listing:
            files.append({
                'name': fileobject.filename,
                'is_folder': fileobject.is_folder,
                'filetype': fileobject.filetype
            })
        return render(self.request, 'home.html', {'files': files, 'query': query.get('dir', '')})
