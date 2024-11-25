from django.urls import path
from .views import EmotionView  # 앱 내 views.py의 EmotionView 가져오기

urlpatterns = [
    path('', EmotionView.as_view(), name='emotion-home'),  # /emotions/
    path('<int:id>/', EmotionView.as_view(), name='emotion-detail'),  # /emotions/<id>/
]
