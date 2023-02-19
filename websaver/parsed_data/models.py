from django.db import models

# Create your models here.
class Notice(models.Model):
    id_ = models.AutoField(primary_key=True, name='id')
    num = models.IntegerField()
    link = models.URLField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, default='NEW')

    def __str__(self):
        return self.id_