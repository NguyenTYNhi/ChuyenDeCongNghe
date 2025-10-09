from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Cache API này trong 60 giây (1 phút)
@cache_page(60)
@api_view(['GET'])
def sample_api(request):
    from datetime import datetime
    data = {
        "message": "Dữ liệu này được cache trong 60 giây",
        "server_time": datetime.now().strftime("%H:%M:%S"),
    }
    return Response(data)
