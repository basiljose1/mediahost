from django.conf.urls import url
from core.views import MediaUploadView

urlpatterns = [
    url(r'^$', MediaUploadView.as_view(), name='media_upload'),
    url(r'^files/$', MediaUploadView.as_view(), name='media_view'),
]

