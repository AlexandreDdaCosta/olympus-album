from django.shortcuts import render
from django.views.generic import TemplateView


class AlbumHome(TemplateView):

    def get(self, errors=False, *args, **kwargs):
        context = {}
        return render(self.request, 'album_home.html', context)
