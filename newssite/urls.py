"""
URL configuration for newssite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views as article_views
from bookings import views as booking_views

urlpatterns = [
    path('', article_views.all_articles, name="home"),
    path('articles/create/', article_views.create_article, name="create_article"),
    path('articles/edit/<article_id>', article_views.edit_article, name="edit_article"),
    path('articles/delete/<article_id>', article_views.delete_article, name="delete_article"),
    path('articles/<article_id>/', article_views.view_article, name="view_article"),

    path('bookings/create/', booking_views.create_booking, name="create_booking"),
    path('bookings/edit/<booking_id>', booking_views.edit_booking, name="edit_booking"),
    path('admin/', admin.site.urls),
]
