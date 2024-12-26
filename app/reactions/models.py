from django.db import models
from common.models import CommonModel
from django.db.models import Q, Count

"""
- User: FK
- Video: FK
- reaction(like, dislike, cancel) => 실제 youtube rest api
- 자식이 FK를 갖는다
User : Reaction => 1:N
Video : Reaction => 1:N
"""

class Reaction(CommonModel):
	# user = models.ForeignKey(User) => Circular Import Error 위험
	user = models.ForeignKey('users.User', on_delete=models.CASCADE)
	video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

	LIKE = 1
	DISLIKE = -1
	NO_REACTION = 0

	REACTION_CHOICES = (
		(LIKE, 'Like'),
		(DISLIKE, 'DisLike'),
		(NO_REACTION, "No Reaction")
	)

	# Like(1), DisLike(-1), No_Reation(0)
	reaction = models.IntegerField(
		choices = REACTION_CHOICES,
		default = NO_REACTION
	)

	@staticmethod
	def get_video_reactions(video):
		# aggregate => 여러 개의 쿼리를 동시에 날릴 수 있음
		reactions = Reaction.objects.filter(video=video).aggregate(
			likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)), # reaction = 1
			dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE)), # reaction = -1
		)
		return reactions