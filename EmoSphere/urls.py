from django.contrib.auth.views import LoginView, LogoutView
from emotions.views.auth_views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Emotion API",
        default_version="v1",
        description="API documentation for EmoSphere",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# 간단한 루트 페이지 응답
def home(request):
    return HttpResponse("<h1>Welcome to EmoSphere</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Django 관리자 URL
    path('api/emotions/', include('emotions.urls')),  # emotions 앱 URL을 '/api/emotions/'로 매핑
    path('api/users/login/', LoginView.as_view(), name='api-login'),  # 로그인 URL
    path('api/users/logout/', LogoutView.as_view(), name='api-logout'),  # 로그아웃 URL
    path('', home, name='home'),  # 루트 경로
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]