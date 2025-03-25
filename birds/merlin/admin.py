from django.contrib import admin
from .models import Bird, Detection, Family, Location, Order

# Register your models here.
@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ['common_name', 'slug', 'genus', 'species', 'link']
    list_filter = ['genus']
    search_fields = ['common_name', 'genus', 'species']
    prepopulated_fields = {'slug': ('common_name',)}
    ordering = ['common_name']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin):
    list_display = ['date', 'bird', 'location']
    list_filter = ['date', 'bird', 'location']
    search_fields = ['bird', 'location']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ['order', 'name']
    list_filter = ['order', 'name']
    search_fields = ['name', 'order']
    ordering = ['order', 'name']
    show_facets = admin.ShowFacets.ALWAYS