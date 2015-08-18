from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /winecat/5/
    url(r'^(?P<wine_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<wine_id>[0-9]+)/vineyard/$', views.vineyard, name='vineyard'),
    # ex: /polls/5/vote/
    url(r'^(?P<wine_id>[0-9]+)/varietal/$', views.varietal, name='varietal'),
]