from django.contrib import admin
from .models import Emotion

# Register your models here.

@admin.register(Emotion)
class EmotionAdmin(admin.ModelAdmin):
    list_display = ('user', 'emotion_type', 'timestamp')  # 표시할 필드
    list_filter = ('emotion_type', 'timestamp')  # 필터 옵션
    search_fields = ('user__username', 'content')  # 검색 가능 필드