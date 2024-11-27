from django.urls import path
from .views.emotion_views import EmotionListView, EmotionDetailView, PlanetEmotionView
from .views.auth_views import LoginView
from .views.statistics_views import EmotionStatisticsView
from .views.emotion_burn_views import EmotionBurnView
from .views.profile_views import UserProfileView

urlpatterns = [
    # 사용자 인증 관련 URL
    path('users/login/', LoginView.as_view(), name='api-login'),  # /api/users/login/
    path('users/logout/', LoginView.as_view(), name='api-logout'),  # /api/users/logout/

    # 감정 데이터 관리
    path('', EmotionListView.as_view(), name='emotion-list'),  # /api/emotions/
    path('<int:id>/', EmotionDetailView.as_view(), name='emotion-detail'),  # /api/emotions/<id>/

    # 감정 소멸
    path('burn/', EmotionBurnView.as_view(), name='emotion-burn'),

    # 행성 조회
    path('planets/', PlanetEmotionView.as_view(), name='emotion-planets'),

    # 감정 통계
    path('statistics/<int:user_id>/', EmotionStatisticsView.as_view(), name='emotion-statistics'),
]
