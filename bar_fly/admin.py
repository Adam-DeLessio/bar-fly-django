from django.contrib import admin

# Register your models here.

from .models import Ingredient
admin.site.register(Ingredient)

from .models import Recipe
admin.site.register(Recipe)