from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Avg
from rest_framework import status
from ..models import Emotion

class EmotionStatisticsView(APIView):
    def get(self, request, user_id):
        # 사용자 데이터 필터링
        emotions = Emotion.objects.filter(user_id=user_id)
        if not emotions.exists():
            return Response({"error": "No data found for this user."}, status=status.HTTP_404_NOT_FOUND)
        
        # 감정 통계 계산
        most_frequent = emotions.values('emotion_type').annotate(count=Count('id')).order_by('-count').first()
        avg_intensity = emotions.aggregate(avg_intensity=Avg('intensity'))

        return Response({
            "most_frequent_emotion": most_frequent['emotion_type'] if most_frequent else None,
            "average_intensity": avg_intensity['avg_intensity'],
        }, status=status.HTTP_200_OK)
