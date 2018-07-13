from django.contrib import admin
from stutens_manage import models
# Register your models here.
class class_id(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(models.Classes, class_id)
admin.site.register(models.Teachers)
admin.site.register(models.Students)