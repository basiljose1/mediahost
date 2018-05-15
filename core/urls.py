from django.conf.urls import url
from core.views import MediaUploadView, MediaHierarchyView

urlpatterns = [
    url(r'^$', MediaUploadView.as_view(), name='media_upload'),
    url(r'^files/$', MediaHierarchyView.as_view(), name='media_view'),
]

