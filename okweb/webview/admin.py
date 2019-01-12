from django.contrib import admin

from .models import Website
from .models import Category

# Register your models here.

models = (
    Website,
    Category,
)
admin.site.register(models)
