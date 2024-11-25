from rest_framework import serializers
from emotions.models import Emotion

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = '__all__'  # 모든 필드 포함
