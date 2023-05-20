from django.urls import path

from django_album_olympus.views import AlbumHome

urlpatterns = [
    path(r'', AlbumHome.as_view(), name='album_home'),
]
