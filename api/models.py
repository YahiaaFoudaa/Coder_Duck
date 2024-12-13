from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def set_password(self, password):
        self.password = make_password(password)
        self.save()

    def check_password(self, password):
        return check_password(password, self.password)
    
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextChoices('Status', 'DRAFT PUBLISHED')


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(blank=False)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
