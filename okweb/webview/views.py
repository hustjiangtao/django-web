from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from .models import Website

# Create your views here.


@require_http_methods(["GET"])
def add_website(request):
    pass


@require_http_methods(["GET"])
def index(request):
    websites = Website.objects.filter()
    result = {
        'msg': 'ok',
        'code': '200',
        'data': [{
            'name': x.website_name,
            'url': x.website_url,
            'favicon': f"http://favicon.byi.pw/?url={x.website_url}",
            'create_time': x.website_create_time,
        } for x in websites]*10,
    }
    return JsonResponse(data=result)
