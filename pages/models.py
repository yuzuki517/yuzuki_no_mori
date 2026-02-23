# pages/models.py
from django.db import models

class Inquiry(models.Model):
    name = models.CharField("お名前", max_length=50)
    email = models.EmailField("メールアドレス")
    subject = models.CharField("件名", max_length=100)
    message = models.TextField("お問い合わせ内容")
    created_at = models.DateTimeField("送信日時", auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.name})"
