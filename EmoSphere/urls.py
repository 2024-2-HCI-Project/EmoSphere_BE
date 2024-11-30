from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        title="Emotion API",
        default_version="v1",
        description="API documentation for EmoSphere",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# 기본 루트 응답
def home(request):
    return HttpResponse("<h1>Welcome to EmoSphere</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('api/', include('emotions.urls')),  # emotions 앱으로 모든 API 위임
    path('', home, name='home'),  # 루트 경로
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
