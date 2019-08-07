# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Categories,SubCategories,ProductModel,Stock,Size
# Register your models here.


admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(ProductModel)
admin.site.register(Size)
admin.site.register(Stock)