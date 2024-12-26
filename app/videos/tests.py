from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse # urlpatterns => name을 기반으로 url값을 불러온다
from django.core.files.uploadedfile import SimpleUploadedFile # File Test용

from users.models import User
from videos.models import Video

class VideoAPITestCase(APITestCase):
	# setUp => 테스트 코드 케이스가 실행 되기 전 가장 먼저 실행되는 함수
	# 테스트 전 데이터를 생성하는 역할
	# (1) 유저 생성 및 로그인 -> (2) 비디오 생성/수정/삭제
	def setUp(self):
		# 회원가입
		self.user = User.objects.create_user( # self를 써줌으로써 전역으로 만들어 줌
			email='asd@gmail.com',
			password='password123'
		)

		# 로그인
		# self.client.login(email='asd@gmail.com', passwrod='password123')
		# -> 익명 유저라서 serializer.save()에서 문제가 생김
		self.client.force_authenticate(user=self.user) # 강제로 인증시켜줌

		# 비디오 생성
		self.video= Video.objects.create(
			title = 'First video title',
			link = 'http://www.test.com',
			user = self.user,
		)


	# 전체 비디오 조회
	# api/v1/videos [GET]
	def test_video_list_get(self):
		url = reverse('video-list') # api/v1/videos
		res = self.client.get(url) # setUp에서 로그인한 유저가 url로 get 요청을 보냄, views의 API를 통함

		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertTrue(len(res.data) > 0) # res.data => list, 비디오가 0개 초과인가?

		for video in res.data:
			self.assertIn('title', video)

	# 비디오 생성
	# api/v1/videos [POST]
	def test_video_list_post(self):
		url = reverse('video-list')
		data = {
			'title': 'My test video title',
			'link': 'http://www.test.com',
			'category': 'Development',
			'thumbnail': 'http://www.test.com',
			'video_file': SimpleUploadedFile('test.mp4', b'file_content', 'video/mp4'),
			# b 문자열 => 바이트 문자열
			# SimpleUploadedFile의 content는 바이트 문자열로 줘야한다.
			# - HTTP를 통해 파일이 업로드되면 server에서 파일을 문자열이 아니라 바이너리 데이터로 받음
			'user': self.user.pk
		}

		res = self.client.post(url, data) # VideoList [POST]

		self.assertEqual(res.status_code, status.HTTP_201_CREATED)
		self.assertEqual(res.data['title'], 'My test video title')




	# 특정 비디오 조회
	# api/v1/videos/{video_id} [GET]
	def test_video_detail_get(self):
		url = reverse('video-detail', kwargs={'pk': self.video.pk})
		res = self.client.get(url)

		self.assertEqual(res.status_code, status.HTTP_200_OK)

	# 특정 비디오 업데이트
	# api/v1/videos/{video_id} [PUT]
	def test_video_detail_put(self):
		url = reverse('video-detail', kwargs={'pk': self.video.pk})
		data = {
			'title': 'Updated video title',
			'link': 'http://www.test.com',
			'category': 'Development',
			'thumbnail': 'http://www.test.com',
			'video_file': SimpleUploadedFile('test.mp4', b'file_content', 'video/mp4'),
			'user': self.user.pk
		}

		res = self.client.put(url, data)
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertEqual(res.data['title'], 'Updated video title')

	# 특정 비디오 삭제
	# api/v1/videos/{video_id} [DELETE]
	def test_video_detail_delete(self):
		url = reverse('video-detail', kwargs={'pk': self.video.pk})
		res = self.client.delete(url)
		self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
		res = self.client.get(url)
		self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)