from django.db import models
from lib.models import BaseModel
from django.contrib.auth.models import User
from post.models import Post


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', verbose_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment', verbose_name='post')
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='reply_comment', verbose_name='reply', null=True, blank=True
    )
    is_reply = models.BooleanField(default=False, verbose_name='is reply')
    body = models.TextField(max_length=140)

    def __str__(self):
        return f"{self.user} - {self.body[:30]}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment'
        ordering = ('-created_time',)


class Relation(BaseModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', verbose_name='from user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', verbose_name='to user')

    def __str__(self):
        return f"{self.from_user} following {self.to_user}"

    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'
        db_table = 'relation'
        ordering = ('-created_time',)


class Vote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_vote', verbose_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_vote', verbose_name='post')

    def __str__(self):
        return f"{self.user} liked {self.post.title[:30]}"

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
        db_table = 'vote'
        ordering = ('-created_time',)
