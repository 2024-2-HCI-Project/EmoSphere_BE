from django.urls import path
from .views import EmotionView  # 앱 내 views.py의 EmotionView 가져오기
from .views import LoginView

urlpatterns = [
    path('', EmotionView.as_view(), name='emotion-home'),  # /emotions/
    path('<int:id>/', EmotionView.as_view(), name='emotion-detail'),  # /emotions/<id>/
        path('login/', LoginView.as_view(), name='api-login'),
    path('logout/', LoginView.as_view(), name='api-logout'),
]
