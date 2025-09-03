from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.http import HttpResponse, Http404, HttpResponseNotFound
import datetime
import asyncio
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView
from django.urls import reverse
from .models import Book
from django.shortcuts import render
from books.models import Book 

# view trả về ngày giờ hiện tại
def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html lang='en'><body>It is now {now}.</body></html>"
    return HttpResponse(html)
# async view trả về ngày giờ hiện tại
async def async_current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html lang='en'><body>[ASYNC] It is now {now}.</body></html>"
    return HttpResponse(html)


# view demo trả về lỗi 404 nếu không tìm thấy
def demo_404(request):
    raise Http404("Trang không tồn tại")

# view demo với HttpResponseNotFound
from django.http import HttpResponseNotFound
def demo_not_found(request):
    return HttpResponseNotFound("<h1>Page not found</h1>")
def go_to_first_news(request):


    # tự động tạo url tới chi tiết bài news id = 1
    url = reverse("news-detail", args=[1])
    return HttpResponseRedirect(url)

def index(request):
    return HttpResponse("trang chủ news")

def detail(request, news_id):
    return HttpResponse(f"chi tiết bài news id = {news_id}")
#bai 3
# 1. Subclass từ TemplateView
class AboutView(TemplateView):
    template_name = "news/about.html"

# 2. RedirectView
class NewsRedirectView(RedirectView):
    pattern_name = "news-index"  # sẽ redirect sang trang chủ news

# 3. ListView cho model Book
class BookListView(ListView):
    model = Book
    template_name = "news/book_list.html"

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("publication_date")
        response = HttpResponse(
            headers={
                "Last-Modified": last_book.publication_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
            }
        )
        return response

# 4. Async View
class AsyncHelloView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")
#hiện books admin
def book_list(request):
    books = Book.objects.all()  # lấy tất cả book từ db
    return render(request, "news/book_list.html", {"books": books})