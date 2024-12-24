from django.contrib import admin
from .models import Category, Dish

class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image_tag']

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "-"

    image_tag.short_description = 'Image'


admin.site.register(Category)
admin.site.register(Dish, DishAdmin)
