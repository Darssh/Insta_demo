from __future__ import unicode_literals

from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
	post_id = models.AutoField(primary_key=True)
	caption = models.TextField()
	image_path = models.FilePathField(path="/Users/Darsh/Downloads")
	date_created = models.DateTimeField(default=timezone.now)
	date_updated = models.DateTimeField(default=timezone.now)

	class Meta:
		db_table='posts'

class UsersPosts(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE)
	is_owner = models.BooleanField()
	is_liked = models.BooleanField()

	class Meta:
		db_table='users_posts'