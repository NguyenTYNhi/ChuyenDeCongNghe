from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "polls/index.html")


def special_case_2003(request):
    return HttpResponse("Special case: year 2003")


def year_archive(request, year):
    return HttpResponse(f"Year archive: {year}")


def month_archive(request, year, month):
    return HttpResponse(f"Month archive: {year}/{month}")


def article_detail(request, year, month, slug):
    return HttpResponse(f"Article: {year}/{month}, slug={slug}")


def page_with_regex(request, page):
    return HttpResponse(f"Page via regex: {page}")


def reports(request):
    return HttpResponse("Credit reports page")


def charge(request):
    return HttpResponse("Credit charge page")


# Ví dụ dùng reverse trong view
def go_to_2005(request):
    url = reverse("polls:year-archive", args=(2005,))
    return HttpResponseRedirect(url)
