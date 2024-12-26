from rest_framework.urls import path
from .views import SubscriptionsListView, SubscriptionsDetailView

urlpatterns = [
	path('', SubscriptionsListView.as_view(), name='subscriptions-list'),
	path('<int:pk>/', SubscriptionsDetailView.as_view(), name='subscriptions-detail'),
]