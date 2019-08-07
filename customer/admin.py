# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import customer_registeration_model,MyWalletModal,MessageModal
# Register your models here.


admin.site.register(customer_registeration_model)
admin.site.register(MyWalletModal)
admin.site.register(MessageModal)

