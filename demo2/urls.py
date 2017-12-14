from django.conf.urls import url
from . import views

app_name = 'demo2'

urlpatterns = [
    # ex: /demo2/
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    # ex: /demo2/5/
    url(r'^(?P<fund_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /demo2/5/results/
    url(r'^(?P<fund_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /demo2/5/vote/
    url(r'^(?P<fund_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^download_html/$', views.download_html, name='download_html'),
]