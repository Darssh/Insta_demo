from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	user_id = models.AutoField(primary_key=True)
	phone = models.BigIntegerField(unique=True, null=True)
	last_ip = models.CharField(max_length=45)
	date_created = models.DateTimeField(default=timezone.now)
	date_updated = models.DateTimeField(default=timezone.now)

	class Meta:
		db_table='user'


class UserInformation(models.Model):
	SEX_TAGS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Specified'),
    )

	user = models.OneToOneField(User)
	full_name = models.CharField(max_length=255, null=True)
	first_name = models.CharField(max_length=255, null=True)
	last_name = models.CharField(max_length=255, null=True)
	sex = models.CharField(max_length=1, choices=SEX_TAGS, default='N')
	date_updated = models.DateTimeField(default=timezone.now)

	class Meta:
		db_table='user_information'


class UserOtherInformation(models.Model):
	user = models.OneToOneField(User)
	website = models.CharField(max_length=255)
	bio = models.CharField(max_length=255)
	date_updated = models.DateTimeField(default=timezone.now)

	class Meta:
		db_table='user_other_information'
