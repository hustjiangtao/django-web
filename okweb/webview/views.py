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
        'data': [
            {
                'name': '常用推荐',
                'sites': [{
                    'name': x.website_name,
                    'url': x.website_url,
                    'logo': f"http://favicon.byi.pw/?url={x.website_url}",
                    'desc': x.website_name*5,
                    'create_time': x.website_create_time,
                } for x in websites]*2,
            },
            {
                'name': '实用工具',
                'sites': [{
                    'name': x.website_name,
                    'url': x.website_url,
                    # 'logo': f"http://favicon.byi.pw/?url={x.website_url}",
                    'logo': f"https://www.baidu.com/favicon.ico",
                    'desc': x.website_name*5,
                    'create_time': x.website_create_time,
                } for x in websites],
            },
        ]
    }
    return JsonResponse(data=result)
