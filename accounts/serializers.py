from .models import User
from django.contrib.auth import get_user_model

from rest_framework import serializers

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('user_id', 'username', 'email', 'phone')
		write_only_fields = ('password',)
		read_only_fields = ('user_id',)

	def create(self, validated_data):
		print(validated_data)
		user = UserModel.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			phone=validated_data['phone']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user