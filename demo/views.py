from django.shortcuts import render

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

