from django.test import TestCase
from django.contrib.auth.models import User
from emotions.models import Emotion
from django.utils.timezone import now, timedelta

class EmotionAPITestCase(TestCase):
    def setUp(self):
        # 중복 방지: 기존 사용자 삭제
        User.objects.filter(username="testuser").delete()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

    def test_login(self):
        response = self.client.post('/api/emotions/users/login/', {"username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_create_emotion(self):
        data = {
            "emotion_type": "happiness",
            "intensity": 80,
            "content": "Feeling great!"
        }
        response = self.client.post('/api/emotions/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["emotion_type"], "happiness")

    def test_burn_emotion(self):
        emotion = Emotion.objects.create(
            user=self.user, emotion_type="happiness", intensity=80, content="Feeling great!"
        )
        response = self.client.post('/api/emotions/burn/', {"emotion_id": emotion.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["emotion"]["status"], "burned")

    def test_planet_emotions(self):
        emotion = Emotion.objects.create(
            user=self.user, emotion_type="happiness", intensity=80, content="Feeling great!", 
            status="burned", burned_at=now() - timedelta(days=8)
        )
        response = self.client.get('/api/emotions/planets/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()["planets"]) > 0)
