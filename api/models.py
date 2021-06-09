from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    object_url = models.FileField(upload_to='urls/')
    retsept_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name
