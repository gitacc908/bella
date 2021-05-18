from django.contrib import admin

from .models import (
    News, About, DeliveryInfo, Contact, FAQ
)

admin.site.register(News)
admin.site.register(About)
admin.site.register(DeliveryInfo)
admin.site.register(Contact)
admin.site.register(FAQ)
