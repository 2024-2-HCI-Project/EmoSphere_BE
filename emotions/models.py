from django.db import models
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.models import User

class Emotion(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),  # 기본 상태 (소멸 전)
        ('burned', 'Burned'),  # 소멸 상태
        ('planet', 'Planet'),  # 행성으로 변환된 상태
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion_type = models.CharField(max_length=50)
    intensity = models.IntegerField(null=True, blank=True)  # 필드 비워도 에러 없음
    input_mode = models.CharField(max_length=10, choices=[("text", "Text"), ("voice", "Voice")], default="text")
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="active")
    timestamp = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')  # 감정 상태
    burned_at = models.DateTimeField(blank=True, null=True)  # 소멸된 시각

    def __str__(self):
        return f"{self.emotion_type} ({self.user.username})"

    @property
    def is_ready_for_planet(self):
        """
        감정이 소멸 후 일주일이 지나면 행성으로 변환 가능 여부 반환
        """
        if self.status == 'burned' and self.burned_at:
            return now() >= self.burned_at + timedelta(days=7)
        return False
