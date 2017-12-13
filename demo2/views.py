
import logging

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.template import loader

from demo2.models import FundInfo

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "demo2/index.html"

    def get(self, request, *args, **kwargs):
        logger.info("IndexView")
        return super().get(request, *args, **kwargs)

def index(request):
    latest_fundinfo_list = FundInfo.objects.order_by('-update_time')[:5]
    template = loader.get_template('demo2/index.html')
    context = {
        'latest_fundinfo_list': latest_fundinfo_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, fund_id):
    return HttpResponse("You're looking at fund %s." % fund_id)

def results(request, fund_id):
    response = "You're looking at the results of fund %s."
    return HttpResponse(response % fund_id)

def vote(request, fund_id):
    return HttpResponse("You're voting on fund %s." % fund_id)

