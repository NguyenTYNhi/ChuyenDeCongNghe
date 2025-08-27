from django.urls import path, re_path, register_converter, include
from . import views

# --- custom converter ---
class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value

# đăng ký converter
register_converter(FourDigitYearConverter, "yyyy")

app_name = "polls"
urlpatterns = [
    # index
    path("", views.index, name="index"),

    # ví dụ URL dispatcher cơ bản
    path("articles/2003/", views.special_case_2003, name="special-2003"),
    path("articles/<int:year>/", views.year_archive, name="year-archive"),
    path("articles/<int:year>/<int:month>/", views.month_archive, name="month-archive"),
    path(
        "articles/<int:year>/<int:month>/<slug:slug>/",
        views.article_detail,
        name="article-detail",
    ),

    # ví dụ custom converter
    path("articles/<yyyy:year>/special/", views.year_archive, name="special-year"),

    # ví dụ regex
    re_path(r"^regex/(?P<page>[0-9]+)/$", views.page_with_regex, name="regex-page"),
]

# --- include lồng nhau ---
credit_patterns = [
    path("reports/", views.reports, name="reports"),
    path("charge/", views.charge, name="charge"),
]

urlpatterns += [
    path("credit/", include((credit_patterns, "polls"), namespace="credit")),
]
