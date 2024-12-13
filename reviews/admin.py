from django.contrib import admin
from .models import Category, MovieReview, TVReview, GameReview

# Register your models here.
admin.site.register(Category)
admin.site.register(MovieReview)
admin.site.register(TVReview)
admin.site.register(GameReview)