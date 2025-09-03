from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="news-index"),
    path("first/", views.go_to_first_news, name="news-first"),
    path("<int:news_id>/", views.detail, name="news-detail"),
]
