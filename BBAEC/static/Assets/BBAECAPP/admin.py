from django.contrib import admin
from BBAECAPP.models import banquet,menu,dishes

# Register your models here.

class BanquetAdmin(admin.ModelAdmin):
    list_display=['id','name','location','Address','rent','is_active']

class MenuAdmin(admin.ModelAdmin):
    list_display=['id','name','package','is_active']

class DishesAdmin(admin.ModelAdmin):
    list_display=['id','name','price','mid']
    list_filter=['mid','price']

admin.site.register(banquet,BanquetAdmin)
admin.site.register(menu,MenuAdmin)
admin.site.register(dishes,DishesAdmin)
