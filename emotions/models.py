from django.db import models
from django.conf import settings

class Emotion(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 사용자 모델과 연결
        on_delete=models.CASCADE
    )
    emotion_type = models.CharField(max_length=50)
    intensity = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='uploads/emotions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.emotion_type} ({self.intensity})"
