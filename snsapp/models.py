from django.db import models

# Create your models here.
class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to='')
    good =models.IntegerField()
    read =models.IntegerField()
    readtext = models.TextField()

    # admin画面の表示
    def __str__(self):
        return self.title
