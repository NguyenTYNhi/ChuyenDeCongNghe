from django.urls import path
from . import views
from django.urls import path, register_converter
from .converters import FourDigitYearConverter

# đăng ký converter
register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("articles/<yyyy:year>/", views.year_archive, name="year-archive"),
    path("articles/<yyyy:year>/<int:month>/<slug:slug>/", views.article_detail, name="article-detail"),
]
urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
]
