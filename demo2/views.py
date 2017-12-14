
import logging

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.template import loader

from demo2.models import FundInfo, PageContent
from .spider import util, mstar_fund
from django.utils import timezone

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "demo2/index.html"

    def get(self, request, *args, **kwargs):
        logger.info("IndexView")
        return super().get(request, *args, **kwargs)

def index(request):
    latest_page_list = PageContent.objects.order_by('-update_time')[:5]
    template = loader.get_template('demo2/index.html')  # 获取模版
    context = {
        'latest_page_list': latest_page_list,   # 模版参数赋值
    }
    return HttpResponse(template.render(context, request))  # 渲染

def funds(request):
    latest_fundinfo_list = FundInfo.objects.order_by('-update_time')[:5]
    template = loader.get_template('demo2/funds.html')  # 获取模版
    context = {
        'latest_fundinfo_list': latest_fundinfo_list,   # 模版参数赋值
    }
    return HttpResponse(template.render(context, request))  # 渲染

def detail(request, fund_id):
    return HttpResponse("You're looking at fund %s." % fund_id)

def results(request, fund_id):
    response = "You're looking at the results of fund %s."
    return HttpResponse(response % fund_id)

def vote(request, fund_id):
    return HttpResponse("You're voting on fund %s." % fund_id)

def download_html(request):
    url_str = request.POST['url']
    html = util.getHtml(url_str)

    old_pc = None
    try:
        old_pc = PageContent.objects.get(url=url_str)
    except PageContent.DoesNotExist:
        pass

    if old_pc != None:
        old_pc.content = html
        old_pc.update_time = timezone.now()
        old_pc.save()
    else:
        pc = PageContent(url=url_str, content=html, update_time=timezone.now())
        pc.save()

    return HttpResponse("download_html %s\n%s" % (url_str, html))


def analyze_page(request):
    pageid = request.POST['pageid']

    try:
        pc = PageContent.objects.get(id=pageid)
        mstar_fund.analyContent(pc.content)
        return HttpResponse("analyze done.")
    except PageContent.DoesNotExist:
        return HttpResponse("page not fund. pageid<%s>" % pageid)

