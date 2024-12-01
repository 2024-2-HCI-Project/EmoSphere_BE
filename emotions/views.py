from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Emotion
from .serializers import EmotionSerializer
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@ensure_csrf_cookie
def csrf_token_view(request):
    """
    CSRF 토큰을 반환하는 뷰
    """
    return JsonResponse({"csrfToken": request.META.get("CSRF_COOKIE")})

class EmotionView(APIView):
    # POST 요청 처리: 새 감정 데이터 저장
    def post(self, request):
        data = request.data.copy()  # request 데이터를 복사하여 수정 가능하게 만듦
        data['user'] = request.user.id

        # intensity 필드가 없는 경우 기본값 설정 (필요하면 사용)
        if 'intensity' not in data:
            data['intensity'] = None
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
