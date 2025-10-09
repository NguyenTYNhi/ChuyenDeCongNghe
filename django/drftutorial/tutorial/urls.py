from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views   # 👈 import views trong app quickstart

# tạo router tự động cho các ViewSet
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # /users/ và /groups/ sẽ được map từ đây
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
