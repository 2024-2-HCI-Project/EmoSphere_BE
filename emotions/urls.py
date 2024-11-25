from django.urls import path
from .views.emotion_views import EmotionListView, EmotionDetailView
from .views.auth_views import LoginView

urlpatterns = [
    # Emotion 관련 URL
    path('emotions/', EmotionListView.as_view(), name='emotion-list'),  # /emotions/
    path('emotions/<int:id>/', EmotionDetailView.as_view(), name='emotion-detail'),  # /emotions/<id>/

    # 사용자 인증 관련 URL
    path('api/users/login/', LoginView.as_view(), name='api-login'),  # /api/users/login/
    path('api/users/logout/', LoginView.as_view(), name='api-logout'),  # /api/users/logout/
]