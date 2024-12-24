from django.db import models
from common.models import CommonModel
"""
- User: FK
- Video: FK
- content
- like
- dislike
User : Comment => 1:N
Video : Comment => 1:N
"""
class Comment(CommonModel):
	user = models.ForeignKey('users.User', on_delete=models.CASCADE)
	video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

	# 리액션과 나눈 이유
	# reaction => 나중에 학습시켜서 추천 알고리즘을 띄우기 위함
	# comment의 like, dislike는 단순히 숫자를 표기하기 위함
	content = models.TextField()
	like = models.PositiveIntegerField(default=0)
	dislike = models.PositiveIntegerField(default=0)

	# 대댓글
	# parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE) # 부모댓글인지 확인