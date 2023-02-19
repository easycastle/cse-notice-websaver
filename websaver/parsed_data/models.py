from django.db import models

# Create your models here.
class Notice(models.Model):
    num = models.IntegerField()
    link = models.URLField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    content = models.TextField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=3, default='NEW')

    def __str__(self):
        return str(self.num)