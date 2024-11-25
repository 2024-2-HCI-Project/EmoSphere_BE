from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Emotion

class EmotionBurnView(APIView):
    def post(self, request):
        emotion_id = request.data.get('emotion_id')
        emotion = Emotion.objects.filter(id=emotion_id, user=request.user).first()

        if not emotion:
            return Response({"error": "Emotion not found or not authorized"}, status=status.HTTP_404_NOT_FOUND)

        # 감정 소멸 처리 (여기서는 단순 삭제로 구현)
        emotion.delete()
        return Response({"message": "Emotion burned successfully!"}, status=status.HTTP_200_OK)
