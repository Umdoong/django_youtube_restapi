from django.db import models
from common.models import CommonModel

"""
- User: FK => subscriber(구독을 하는 사람)
- User: FK => subscribed_to(구독을 받는 사람)
"""

# User : User(Subscriber) => N:N
# User : User(Subscribed_to) => N:N
class Subscription(CommonModel):
	subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
	subscribed_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')
	# 역참조할 때 헷갈리니까 헷갈리지 않게 related_name을 지정해준다.
	# 특정 사용자를 구독하는 사람 보기 => user.subscribers.all()
	# 내가 구독한 사람을 전부 가져오기 => user.subscriptions.all()