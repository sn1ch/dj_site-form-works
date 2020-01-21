from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')
    ordering = ('-id',)
    search_fields = ('brand', 'model')
    list_filter = ('brand', 'model')
    pass


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('car', 'title')
    ordering = ('-id',)
    search_fields = ('title', 'car__model')
    list_filter = ('car__model',)
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
