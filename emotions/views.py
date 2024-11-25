from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from rest_framework import status
from .models import Emotion
from .serializers import EmotionSerializer

class EmotionView(APIView):
    # GET 요청 처리: 로그인한 사용자의 감정 데이터 조회
    def get(self, request):
        emotions = Emotion.objects.filter(user=request.user)  # 로그인한 사용자만 필터링
        serializer = EmotionSerializer(emotions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST 요청 처리: 감정 데이터 저장, 로그인한 사용자와 연결
    def post(self, request):
        data = request.data.copy()  # 요청 데이터를 복사하여 수정 가능하게 만듦
        data['user'] = request.user.id  # 현재 로그인한 사용자의 ID를 추가
        serializer = EmotionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # 유효한 데이터를 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(login_required, name='dispatch')
class EmotionView(APIView):
    def get(self, request):
        emotions = Emotion.objects.filter(user=request.user)
        serializer = EmotionSerializer(emotions, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = EmotionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class LoginView(APIView):
    def get(self, request):
        return Response({"message": "Use POST to log in."}, status=200)

    def post(self, request):
        # 로그인 처리
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"}, status=200)
        return Response({"error": "Invalid credentials"}, status=400)

    def delete(self, request):
        #로그아웃 처리
        logout(request)
        return Response({"message": "Logout successful"}, status=200)
    
    