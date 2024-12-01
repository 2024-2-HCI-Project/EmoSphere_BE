from rest_framework import serializers
from emotions.models import Emotion

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ['user', 'emotion_type', 'input_mode', 'description', 'timestamp']
        extra_kwargs = {
            'description': {'required': False},  # description을 필수로 요구하지 않음
        }
        read_only_fields = ['timestamp']  # timestamp는 읽기 전용

