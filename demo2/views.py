
import logging

# Create your views here.
from django.views import generic

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "demo2/index.html"

    def get(self, request, *args, **kwargs):
        logger.info("IndexView")
        return super().get(request, *args, **kwargs)

