# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


import upyun

from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible

from .do_tinyfy import buffer_tinyfy


@deconstructible
class UpyunStorage(Storage):
    from django.conf import settings
    BUCKET_NAME = settings.UPYUN["BUCKET_NAME"]
    USER_NAME = settings.UPYUN["USER_NAME"]
    PASSWORD = settings.UPYUN["PASSWORD"]
    BASE_URL = settings.UPYUN["BASE_URL"]
    up = upyun.UpYun(BUCKET_NAME, username=USER_NAME, password=PASSWORD, timeout=30)

    def _save(self, name, content):
        # name here is "static/%Y/%m/%d/" (MEDIA_ROOT + upload_to)
        # save suffix url without static domain
        # full_url = self.BASE_URL + name
        suffix_url = '/' + name
        try:
            file = content.read()
            # tinyfy by tinypng, only .png & .jpg files
            if content.content_type in ("image/png", "image/jpeg"):
                file = buffer_tinyfy(source_data=file)
            res = self.up.put(name, file)
        except Exception as e:
            raise
        # return full_url
        return suffix_url

    def exists(self, name):
        try:
            self.up.getinfo(name)
        except Exception as e:
            return False
        return False

    def listdir(self, path):
        pass

    def size(self, name):
        return 0

    def url(self, name):
        # name here is the full_url
        return name
