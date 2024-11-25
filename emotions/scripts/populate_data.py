from django.utils.timezone import now
from emotions.models import Emotion
from django.contrib.auth.models import User

def run():
    user = User.objects.first()
    if not user:
        user = User.objects.create_user(username='testuser', password='password123')

    Emotion.objects.create(
        user=user,
        emotion_type="happiness",
        intensity=80,
        content="I felt great today!",
        timestamp=now()
    )
    print("Emotion data created successfully!")
