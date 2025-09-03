from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def go_to_first_news(request):
    # tự động tạo url tới chi tiết bài news id = 1
    url = reverse("news-detail", args=[1])
    return HttpResponseRedirect(url)

def index(request):
    return HttpResponse("trang chủ news")

def detail(request, news_id):
    return HttpResponse(f"chi tiết bài news id = {news_id}")
