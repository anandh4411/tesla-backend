from django.contrib import admin
from home.models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','category','description','product_description','image']
    list_editable = ['title','price','category','description','product_description','image']