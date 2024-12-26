from rest_framework.serializers import ModelSerializer
from users.models import User


class UserInfoSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'email', 'nickname')