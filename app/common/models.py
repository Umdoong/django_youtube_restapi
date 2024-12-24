from django.db import models

class CommonModel(models.Model):
	# 생성시간 고정
	created_at = models.DateTimeField(auto_now_add=True)
	# 업데이트 될 때마다 변경
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True