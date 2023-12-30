from django.contrib import admin
from  service.models import Service

class Serviceadmin(admin.ModelAdmin):
    d =('comment')
admin.site.register(Service,Serviceadmin)
# Register your models here.
