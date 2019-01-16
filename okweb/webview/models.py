from django.db import models

from .utils.upyun_storage import UpyunStorage

# Create your models here.


def get_default_avatar(email, size=40):
    # import hashlib
    # import urllib.parse
    # return "https://www.gravatar.com/avatar/%s?%s" % (
    #     hashlib.md5(email.lower().encode()).hexdigest(), urllib.parse.urlencode({'s': str(size)}))
    return 'https://www.gravatar.com/avatar/86002c942ce536ce28e806d42edcdfef?s=40'


class Website(models.Model):
    website_name = models.CharField(max_length=64)
    website_url = models.URLField(max_length=255)
    website_logo = models.URLField(max_length=255, default=get_default_avatar('jiangtao.work@gmail.com'))
    website_desc = models.CharField(max_length=255, blank=True)
    website_category = models.SmallIntegerField(db_index=True, default=0)
    website_create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. {self.website_name} ({self.website_url})"


class Category(models.Model):
    name = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. {self.name}"


class StaticFile(models.Model):
    name = models.CharField(max_length=40)
    url = models.FileField(upload_to="static/%Y/%m/%d/", storage=UpyunStorage())
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. {self.name}: {self.url}"
