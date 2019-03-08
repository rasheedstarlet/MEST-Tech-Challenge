from django.contrib import admin

# Register your models here.
from .models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'price', 'address', 'furnished', 'created']
    list_filter = ['address', 'created', 'price']
    list_editable = ['price']
    #prepopulated_fields = {'slug': ('name',)}


admin.site.register(House, HouseAdmin)
