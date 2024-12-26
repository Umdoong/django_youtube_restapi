from rest_framework.exceptions import NotFound
from rest_framework.views import APIView, Response
from rest_framework import status

from .models import Video
from .serializers import VideoListSerializer, VideoDetailSerializer


# Video와 관련된 REST API
# 1. VideoList => api/v1/videos
# [GET] : 전체 비디오 목록 조회
# [POST] : 새로운 비디오 생성
# [PUT], [DELETE] : X

class VideoList(APIView):
	def get(self, request):
		videos = Video.objects.all() # objects => QuerySet[Video, Video...]

		# objects -> Json (직렬화)
		serializer = VideoListSerializer(videos, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		user_data = request.data
		# Json => objects(역직렬화)
		serializer = VideoListSerializer(data=user_data)
		if serializer.is_valid():
			serializer.save(user=request.user) # 로그인을 진행한 상태니까 요청을 보낸 user의 데이터도 필요
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# 2. VideoDetail => api/v1/videos/{video_id}
# [GET] : 특정 비디오 조회
# [POST] : X -> video_id는 db를 통해 받기 때문에 client에게 POST를 받지 않는다
# [PUT] : 특정 비디오 업데이트
# [DELETE] : 특정 비디오 삭제

class VideoDetail(APIView):
	def get(self, request, pk):
		try:
			video_obj = Video.objects.get(pk=pk)

		except Video.DoesNotExist:
			raise NotFound

		serializer = VideoDetailSerializer(video_obj)

		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, pk):
		video_obj = Video.objects.get(pk=pk)
		user_data = request.data # 업데이트 데이터

		serializer = VideoDetailSerializer(video_obj, data=user_data)
		serializer.is_valid(raise_exception=True) # if문말고 이렇게도 가능
		serializer.save()

		return Response(serializer.data, status=status.HTTP_200_OK)


	def delete(self, request, pk):
		video_obj = Video.objects.get(pk=pk)
		video_obj.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)