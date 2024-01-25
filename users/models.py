from django.db import models

# Create your models here.
class Users(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    email = models.EmailField(max_length=254)
    is_instra_ss = models.BooleanField(default=False)
    yt_username = models.CharField(max_length=254, blank=True, null=True)
    instra_username = models.CharField(max_length=254, blank=True, null=True)
    is_ytc_ss = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=False)
    is_following = models.BooleanField(default=False)
    yt_url = models.CharField(max_length=254, blank=True, null=True)