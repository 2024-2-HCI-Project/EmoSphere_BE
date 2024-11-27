from django.db import models
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta

class Emotion(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),  # 기본 상태 (소멸 전)
        ('burned', 'Burned'),  # 소멸 상태
        ('planet', 'Planet'),  # 행성으로 변환된 상태
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 사용자 모델과 연결
        on_delete=models.CASCADE
    )
    emotion_type = models.CharField(max_length=50)  # 감정의 종류 (예: happiness, anger 등)
    intensity = models.PositiveSmallIntegerField()  # 감정 강도 (0~100)
    timestamp = models.DateTimeField(auto_now_add=True)  # 생성 시각
    content = models.TextField(blank=True, null=True)  # 감정 내용
    attachment = models.FileField(upload_to='uploads/emotions/', blank=True, null=True)  # 파일 첨부
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터 생성 시각

    # 새로 추가된 필드
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')  # 감정 상태
    burned_at = models.DateTimeField(blank=True, null=True)  # 소멸된 시각

    def __str__(self):
        return f"{self.user.username} - {self.emotion_type} ({self.intensity})"

    @property
    def is_ready_for_planet(self):
        """
        감정이 소멸 후 일주일이 지나면 행성으로 변환 가능 여부 반환
        """
        if self.status == 'burned' and self.burned_at:
            return now() >= self.burned_at + timedelta(days=7)
        return False
