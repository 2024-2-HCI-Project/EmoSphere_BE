=======
# Emosphere - Backend

## 프로젝트 개요
**Emosphere**는 사용자의 감정을 시각적으로 표현하고 관리할 수 있는 AR 기반 감정 관리 플랫폼입니다.  
이 저장소는 **Emosphere**의 백엔드 API를 담당하며, Django 및 Django REST Framework(DRF)를 기반으로 구현되었습니다.

---

## 주요 기능
### 사용자 인증
- **로그인**: 사용자 인증을 통해 서비스에 접근 가능.
- **로그아웃**: 현재 세션 종료.

### 감정 데이터 관리
- **감정 입력**: 사용자가 감정 유형, 강도, 내용을 기록.
- **감정 조회**: 사용자가 기록한 감정 데이터를 조회.

### 감정 소멸
- 감정을 '불태우는' 시각적 효과로 감정을 일시적으로 해소.
- 소멸된 감정은 일주일 후 '행성'으로 복원되어 재조회 가능.

### 감정 통계
- 사용자별 감정 데이터를 분석하여 통계 제공.

---

## 기술 스택
- **언어**: Python
- **프레임워크**: Django, Django REST Framework
- **데이터베이스**: MySQL
- **테스트**: Django TestCase

---

## 설치 및 실행
### 1. 사전 준비
- Python 3.10 이상
- MySQL 데이터베이스 설치 및 설정

### 2. 프로젝트 클론
```bash
git clone https://github.com/2024-2-HCI-Project/EmoSphere_BE.git
cd EmoSphere_BE

### 3. 가상환경 설정 및 패키지 설치
```python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

### 4. 데이터베이스 설정
settings.py 수정: MySQL 정보 업데이트
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'emospheredb',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
`    }
}
>>>>>>> 6ed7433 (API 테스트 완료)
