from django.urls import path
from .views.emotion_views import EmotionListView, EmotionDetailView
from .views.auth_views import LoginView
from .views.statistics_views import EmotionStatisticsView
from .views.emotion_burn_views import EmotionBurnView
from .views.profile_views import UserProfileView

urlpatterns = [
    # 사용자 인증 관련 URL
    path('api/users/login/', LoginView.as_view(), name='api-login'),  # /api/users/login/
    path('api/users/logout/', LoginView.as_view(), name='api-logout'),  # /api/users/logout/

    # 감정 데이터 관리
    path('api/emotions/', EmotionListView.as_view(), name='emotion-list'),  # /emotions/
    path('api/emotions/<int:id>/', EmotionDetailView.as_view(), name='emotion-detail'),  # /emotions/<id>/

    # 감정 소멸
    path('api/emotions/burn/', EmotionBurnView.as_view(), name='emotion-burn'),

    # 감정 통계
    path('api/emotions/statistics/<int:user_id>/', EmotionStatisticsView.as_view(), name='emotion-statistics'),
]