"""
URL configuration for EmoSphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# 간단한 루트 페이지 응답
def home(request):
    return HttpResponse("<h1>Welcome to EmoSphere</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Django 관리자 URL
    path('api/', include('emotions.urls')),  # 'api/' 하위 URL 매핑
    path('emotions/', include('emotions.urls')),  # emotions 앱의 URL 포함(emotions 앱의 URL 패턴을 가져와 /emotions/ 경로로 연결)
    path('', home)

]