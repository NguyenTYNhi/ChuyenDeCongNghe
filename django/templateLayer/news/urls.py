from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="news-index"),
    path("<int:news_id>/", views.detail, name="news-detail"),
]
