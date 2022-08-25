from django.db import models


class Resume(models.Model):
    user = models.ForeignKey('auth.User', related_name='resume', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    grade = models.IntegerField(default=0)
    specialty = models.CharField(max_length=200)
    salary = models.IntegerField(default=0)
    education = models.CharField(max_length=300)
    experience = models.TextField()
    portfolio = models.TextField()
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
