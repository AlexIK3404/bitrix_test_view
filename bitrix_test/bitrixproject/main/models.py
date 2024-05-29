from django.db import models

class StoredRequests(models.Model):
    request = models.CharField('Request', max_length=255)
    text = models.CharField('Text', max_length=255)

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"