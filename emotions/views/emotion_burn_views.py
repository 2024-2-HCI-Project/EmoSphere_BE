from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Emotion
from django.utils.timezone import now

class EmotionBurnView(APIView):
    def post(self, request):
        emotion_id = request.data.get('emotion_id')
        emotion = Emotion.objects.filter(id=emotion_id, user=request.user, status='active').first()

        if not emotion:
            return Response({"error": "Emotion not found or already burned"}, status=status.HTTP_404_NOT_FOUND)

        # 감정 소멸 처리: 상태 변경 및 소멸 시간 기록
        emotion.status = 'burned'
        emotion.burned_at = now()
        emotion.save()

        return Response({
            "message": "Emotion burned successfully!",
            "emotion": {
                "id": emotion.id,
                "emotion_type": emotion.emotion_type,
                "intensity": emotion.intensity,
                "status": emotion.status,
                "burned_at": emotion.burned_at,
            }
        }, status=status.HTTP_200_OK)
