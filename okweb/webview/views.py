from collections import defaultdict

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from .models import Website
from .models import Category

# Create your views here.


@require_http_methods(["GET"])
def add_website(request):
    pass


@require_http_methods(["GET"])
def index(request):
    categorys = Category.objects.filter()
    websites = Website.objects.filter()
    websites_dict = defaultdict(list)
    for x in websites:
        if x:
            websites_dict[x.website_category].append({
                'name': x.website_name,
                'url': x.website_url,
                # 'logo': f"http://favicon.byi.pw/?url={x.website_url}",
                # 'logo': f"https://www.baidu.com/favicon.ico",
                'logo': x.website_logo,
                'desc': x.website_desc,
                'create_time': x.website_create_time,
            })
    group_websites = [
        {
            'name': category.name,
            'sites': websites_dict.get(category.id),
        } for category in categorys if category
    ]
    filter_group_websites = [x for x in group_websites if x.get('sites')]
    result = {
        'msg': 'ok',
        'code': '200',
        'data': filter_group_websites,
    }
    return JsonResponse(data=result)
