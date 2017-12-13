from django.conf.urls import url

from . import views

app_name = 'demo2'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^count_list/$', views.CountListView.as_view(), name='count_list'),
    # url(r'^count_list/add$', views.add, name='add'),
    # url(r'^email$', views.EmailView.as_view(), name='email'),
    # url(r'^email/send$', views.send_email, name='send_email'),
]