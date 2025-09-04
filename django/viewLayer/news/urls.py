from django.urls import path
from . import views

urlpatterns = [
    # bài 1 (news)
    path("", views.index, name="news-index"),
    path("first/", views.go_to_first_news, name="news-first"),
    path("<int:news_id>/", views.detail, name="news-detail"),

    # bài 2 (view function)
    path("time/", views.current_datetime, name="current_datetime"),
    path("async-time/", views.async_current_datetime, name="async_current_datetime"),
    path("error404/", views.demo_404, name="demo_404"),
    path("notfound/", views.demo_not_found, name="demo_not_found"),

    # bai 3 (class-based views)
    path("about/", views.AboutView.as_view(), name="about"),
    path("go-home/", views.NewsRedirectView.as_view(), name="go-home"),
   
    path("async-hello/", views.AsyncHelloView.as_view(), name="async-hello"),
    path('books/', views.book_list, name='book_list'),
]
