# AgriERP/views.py

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

# -----------------------
# Ví dụ cache cho ViewSet
# -----------------------
class UserViewSet(viewsets.ViewSet):
    # Cache URL theo user riêng biệt trong 2 giờ
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, format=None):
        content = {
            "user_feed": "Demo data for user feed"
        }
        return Response(content)

# -----------------------
# Ví dụ cache cho APIView
# -----------------------
class ProfileView(APIView):
    # Cache request theo Authorization header
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, format=None):
        content = {
            "user_feed": "Demo profile feed"
        }
        return Response(content)

# Cache toàn bộ page
class PostView(APIView):
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        content = {
            "title": "Post title",
            "body": "Post content"
        }
        return Response(content)

# -----------------------
# Ví dụ cache cho function-based view
# -----------------------
@cache_page(60 * 15)  # cache 15 phút
@vary_on_cookie
@api_view(["GET"])
def get_user_list(request):
    content = {"user_feed": "Demo user list"}
    return Response(content)
