from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema

class SignUpView(APIView):
    """
    회원가입 API
    
    **Endpoint**: `/users/signup/`
    **Method**: `POST`

    새로운 사용자를 등록합니다.

    **요청 데이터**:
    - `username` (string): 사용자 이름 (필수)
    - `password` (string): 비밀번호 (필수)

    **응답 데이터**:
    - `message` (string): 성공 메시지
    - `user_id` (integer): 생성된 사용자 ID

    **응답 코드**:
    - `201`: 사용자 생성 성공
    - `400`: 잘못된 요청 (필요한 데이터 누락 또는 사용자 이름 중복)
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 유효성 검사
        if not username or not password:
            raise ValidationError({"error": "Username and password are required"})

        # 중복 사용자 확인
        if User.objects.filter(username=username).exists():
            raise ValidationError({"error": "Username already exists"})

        # 사용자 생성
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    """
    로그인 API
    
    **Endpoint**: `/users/login/`
    **Method**: `POST`

    사용자 인증 후 세션을 생성합니다.

    **요청 데이터**:
    - `username` (string): 사용자 이름 (필수)
    - `password` (string): 비밀번호 (필수)

    **응답 데이터**:
    - `message` (string): 성공 메시지

    **응답 코드**:
    - `200`: 로그인 성공
    - `400`: 잘못된 자격 증명
    """
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    """
    로그아웃 API
    
    **Endpoint**: `/users/logout/`
    **Method**: `POST`

    현재 로그인된 사용자의 세션을 종료합니다.

    **응답 데이터**:
    - `message` (string): 성공 메시지

    **응답 코드**:
    - `200`: 로그아웃 성공
    """
    @swagger_auto_schema(
        operation_id="user_logout",
        operation_summary="로그아웃",
        responses={
            200: "Logout successful",
        }
    )
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
