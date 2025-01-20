from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 작성자

    def __str__(self):
        return self.title

