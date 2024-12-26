from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Subscription
from users.models import User
from .serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionsListView(APIView):
	def post(self, request):
		subscriber = request.user # 인증된 유저(나)가 구독을 하는 사람이 된다
		subscribed_to_id = request.data.get('subscribed_to') # {subscribed_to: user_id}

		# 구독대상자 None방지 or 자기 스스로를 구독하는 걸 방지 or 중복적인 구독 방지 / exists() => 데이터가 있으면 True
		if (not subscribed_to_id or subscriber.id == subscribed_to_id
				or Subscription.objects.filter(subscriber=subscriber,
																			subscribed_to_id=subscribed_to_id).exists()):
			return Response({"error": "Invalid subscription request."}, status=status.HTTP_400_BAD_REQUEST)

		# {subscribed_to: 나}, 로그인 중인 인증된 유저가 구독을 시도하는 것
		request.data['subscriber'] = subscriber.id
		serializer = SubscriptionSerializer(data=request.data)
		try:
			serializer.is_valid(raise_exception=True) # == if serializer.is_valid
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		except ValidationError as e:
			return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionsDetailView(APIView):
	def delete(self, request, pk):
		if not pk:
			return Response({"error": "Invalid subscription request."}, status=status.HTTP_400_BAD_REQUEST)
		subscriber = request.user
		# Subscription model에서 subscriber, subscribed_to가 같은 object를 조회, object가 없으면 404 return
		# Q는 좀 더 복잡한 쿼리(AND, OR, NOT 등)을 다룰 수 있게 해준다
		subscription = get_object_or_404(Subscription, Q(subscriber=subscriber) & Q(subscribed_to_id=pk))
		subscription.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)