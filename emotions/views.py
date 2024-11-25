from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Emotion
from .serializers import EmotionSerializer

class EmotionView(APIView):
    # POST 요청 처리: 새 감정 데이터 저장
    def post(self, request):
        serializer = EmotionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET 요청 처리: 감정 데이터 조회
    def get(self, request):
        user_id = request.query_params.get('user_id')  # URL의 쿼리 파라미터로 사용자 ID 필터링
        if user_id:
            emotions = Emotion.objects.filter(user_id=user_id)
        else:
            emotions = Emotion.objects.all()
        serializer = EmotionSerializer(emotions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
