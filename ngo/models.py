from django.db import models

# Create your models here.


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('moderator', 'Moderator'),  # Add more roles as needed
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, null=False)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Work(models.Model):
    Cat = 'education'
    image = models.ImageField(upload_to='image', default='image/default.jpg')
    info = models.TextField(verbose_name="Details", default="ww")
    info2 = models.TextField(verbose_name="Details", default="ww")    
    title = models.CharField(max_length=200, verbose_name="Title", default="ww")
