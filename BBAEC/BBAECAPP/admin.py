from django.contrib import admin
from BBAECAPP.models import banquet,menu,dishes,rating,manager

# Register your models here.

class BanquetAdmin(admin.ModelAdmin):
    list_display = ('name','rent','address','location','rating','is_active')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','name','package','is_active')

class DishesAdmin(admin.ModelAdmin):
    list_display = ('name','price','is_active')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id','name','rating')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name','number','banqid')

admin.site.register(banquet,BanquetAdmin)
admin.site.register(menu,MenuAdmin)
admin.site.register(dishes,DishesAdmin)
admin.site.register(rating,RatingAdmin)
admin.site.register(manager,ManagerAdmin)