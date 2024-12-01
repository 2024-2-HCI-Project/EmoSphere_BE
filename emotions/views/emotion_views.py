from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from ..models import Emotion
from ..serializers import EmotionSerializer
from django.utils.timezone import now


@method_decorator(login_required, name='dispatch')
class EmotionListView(APIView):
    """
    감정 목록 조회 및 생성 API
    """
    def get(self, request):
        """
        GET 요청:
        - 사용자와 연결된 감정 목록을 반환합니다.
        """
        emotions = Emotion.objects.filter(user=request.user)
        serializer = EmotionSerializer(emotions, many=True)
        print(f"[DEBUG] Retrieved {len(emotions)} emotions for user {request.user}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST 요청:
        - 새로운 감정을 생성합니다.
        """
        data = request.data.copy()
        data['user'] = request.user.id

        print(f"[DEBUG] Received data for creation: {data}")

        serializer = EmotionSerializer(data=data)
        if serializer.is_valid():
            # recorded_at 필드 제거
            instance = serializer.save()  # recorded_at 전달하지 않음
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@method_decorator(login_required, name='dispatch')
class EmotionDetailView(APIView):
    """
    개별 감정 조회 및 삭제 API
    """
    def get(self, request, id):
        """
        특정 감정을 조회합니다.
        """
        emotion = Emotion.objects.filter(id=id, user=request.user).first()
        if not emotion:
            print(f"[DEBUG] Emotion with ID {id} not found for user {request.user}")
            return Response({"error": "Emotion not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmotionSerializer(emotion)
        print(f"[DEBUG] Retrieved emotion: {serializer.data}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        """
        특정 감정을 삭제합니다.
        """
        emotion = Emotion.objects.filter(id=id, user=request.user).first()
        if not emotion:
            print(f"[DEBUG] Emotion with ID {id} not found for user {request.user}")
            return Response({"error": "Emotion not found"}, status=status.HTTP_404_NOT_FOUND)

        emotion.delete()
        print(f"[DEBUG] Deleted emotion with ID {id}")
        return Response({"message": "Emotion deleted"}, status=status.HTTP_204_NO_CONTENT)


class PlanetEmotionView(APIView):
    """
    소멸된 감정을 행성으로 변환하는 API
    """
    def get(self, request):
        """
        사용자의 소멸된 감정을 행성으로 변환합니다.
        """
        emotions = Emotion.objects.filter(user=request.user, status='burned')
        planets = []

        print(f"[DEBUG] Found {len(emotions)} burned emotions for user {request.user}")

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
                print(f"[DEBUG] Converted emotion {emotion.id} to planet")

        return Response({"planets": planets}, status=status.HTTP_200_OK)
