from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


import logging

# Create your views here.
from django.views import generic
from .models import Counter

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "demo/index.html"

    def get(self, request, *args, **kwargs):
        logger.info("IndexView")
        return super().get(request, *args, **kwargs)


class CountListView(generic.ListView):
    template_name = "demo/count_list.html"
    context_object_name = 'count_list'
    logger.info("CountListView_init")

    def get_queryset(self):
        return Counter.objects.all()


def add(request):
    t = request.POST['name']
    try:
        c = Counter.objects.get(text=t)
    except Counter.DoesNotExist:
        logger.info("add %s" % t)
        c = Counter(text=t, count=0)
        c.save()
    else:
        c.count += 1
        c.save()
    return HttpResponseRedirect(reverse('demo:count_list'))


