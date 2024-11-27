from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from ..models import Emotion
from ..serializers import EmotionSerializer

@method_decorator(login_required, name='dispatch')
class EmotionListView(APIView):
    def get(self, request):
        emotions = Emotion.objects.filter(user=request.user)
        serializer = EmotionSerializer(emotions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = EmotionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(login_required, name='dispatch')
class EmotionDetailView(APIView):
    def get(self, request, id):
        emotion = Emotion.objects.filter(id=id, user=request.user).first()
        if not emotion:
            return Response({"error": "Emotion not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmotionSerializer(emotion)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        emotion = Emotion.objects.filter(id=id, user=request.user).first()
        if not emotion:
            return Response({"error": "Emotion not found"}, status=status.HTTP_404_NOT_FOUND)
        emotion.delete()
        return Response({"message": "Emotion deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class PlanetEmotionView(APIView):
    def get(self, request):
        # 우주 행성으로 변환 가능한 감정 필터링
        emotions = Emotion.objects.filter(user=request.user, status='burned')
        planets = []

        for emotion in emotions:
            if emotion.is_ready_for_planet:
                emotion.status = 'planet'
                emotion.save()
                planets.append({
                    "id": emotion.id,
                    "emotion_type": emotion.emotion_type,
                    "intensity": emotion.intensity,
                    "status": emotion.status,
                    })

        return Response({"planets": planets}, status=status.HTTP_200_OK)