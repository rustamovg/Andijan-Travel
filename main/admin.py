from django.contrib import admin
from .models import Hotel, HotelPhoto
# Register your models here.

class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 4

class HotelAdmin(admin.ModelAdmin):
    inlines = [ HotelPhotoInline]

admin.site.register(Hotel, HotelAdmin)