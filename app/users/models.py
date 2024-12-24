from django.contrib.auth.models import (
	AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models

"""
- email
- password
- nickname
- is_business
"""

class UserManager(BaseUserManager):
	# 일반 유저 생성 함수
	def create_user(self, email, password):
		if not email:
			raise ValueError('Please enter an email address')

		user = self.model(email=email)
		user.set_password(password)
		user.save()

		return user

	# 슈퍼 유저 생성 함수
	def create_superuser(self, email, password):
		user = self.create_user(email, password)

		user.is_superuser = True
		user.is_staff = True

		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	nickname = models.CharField(max_length=50)
	is_business = models.BooleanField(default=False)

	# Permissions Mixin : 유저의 권한 관리
	is_active = models.BooleanField(default=True) # 계정 활성화 상태
	is_staff = models.BooleanField(default=False) # staff 여부

	USERNAME_FIELD = 'email' # id를 email로 받겠다

	objects = UserManager()

	def __str__(self):
		return f'email: {self.email}, nickname: {self.nickname}'