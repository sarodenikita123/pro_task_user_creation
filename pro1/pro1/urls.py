from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from app1.views import StudentViewSet
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = DefaultRouter()
router.register('stu', StudentViewSet, 'stu'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/', include(router.urls)),
    path('access/', token_obtain_pair),
    path('refresh/', token_refresh),
    path('auth/', include('auth_app.urls'))
]
