from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DemoSerializer

class ValidatorDemoView(APIView):
    def get(self, request):
        serializer = DemoSerializer(data={"number": 10, "slug": "abc"})
        serializer.is_valid()
        return Response(serializer.validated_data)
