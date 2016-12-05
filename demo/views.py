from django.shortcuts import render

# Create your views here.
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "demo/index.html"


def index(request):
    return render(request, "demo/index.html")
