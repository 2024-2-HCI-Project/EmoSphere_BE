from django.urls import path
from emotions.views.auth_views import SignUpView, LoginView, LogoutView
from emotions.views.emotion_views import EmotionListView, EmotionDetailView, PlanetEmotionView
from emotions.views.emotion_burn_views import EmotionBurnView
from emotions.views.statistics_views import EmotionStatisticsView
from .views import csrf_token_view

urlpatterns = [
    path('csrf/', csrf_token_view, name='csrf-token'),

     # 사용자 인증 관련
    path('users/signup/', SignUpView.as_view(), name='user-signup'),  # 회원가입
    path('users/login/', LoginView.as_view(), name='user-login'),  # 로그인
    path('users/logout/', LogoutView.as_view(), name='user-logout'),  # 로그아웃

    # 감정 데이터 관리
    path('emotions/', EmotionListView.as_view(), name='emotion-list'),  # GET: 감정 목록, POST: 새 감정 생성
    path('emotions/<int:id>/', EmotionDetailView.as_view(), name='emotion-detail'),  # GET, DELETE: 특정 감정 처리

    # 감정 소멸
    path('emotions/burn/', EmotionBurnView.as_view(), name='emotion-burn'),

    # 행성 조회
    path('emotions/planets/', PlanetEmotionView.as_view(), name='emotion-planets'),

    # 감정 통계
    path('emotions/statistics/<int:user_id>/', EmotionStatisticsView.as_view(), name='emotion-statistics'),
]
