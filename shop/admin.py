from django.contrib import admin
from.models import *
# Register your models here.
class categdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(categ,categdmin)

class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img']
    list_editable = ['stock','img']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodadmin)