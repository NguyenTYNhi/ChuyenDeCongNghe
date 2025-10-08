from datetime import datetime
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Snippet

from .serializers import SnippetSerializer
from .models import Snippet



# -----------------------------
# CRUD API cho Snippet
# -----------------------------
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# -----------------------------
# API demo caching
# -----------------------------
@cache_page(60)  # Cache trong 60 giây
@api_view(['GET'])
def cached_hello(request):
    data = {
        "message": "Hello, this response is cached for 60 seconds!",
        "server_time": datetime.now().strftime("%H:%M:%S"),
    }
    return Response(data)
