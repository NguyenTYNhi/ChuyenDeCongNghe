from django.shortcuts import render
from django.http import HttpResponse

# Trang chủ news
def index(request):
    context = {"title": "Trang chủ News", "user": "Admin"}
    return render(request, "news/index.html", context)

# Chi tiết bài viết
def detail(request, news_id):
    context = {
        "news_id": news_id,
        "title": f"Chi tiết bài {news_id}",
        "content": "Đây là nội dung bài viết demo."
    }
    return render(request, "news/detail.html", context)
