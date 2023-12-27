# email_app/models.py
from django.db import models

class EmailInfo(models.Model):
    to_email = models.EmailField()
    company_name = models.CharField(max_length=100)
    message_content = models.TextField()

    def __str__(self):
        return self.to_email
