from django.db import models
from django.urls import reverse
from lib.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from category.models import Category
from django.contrib.auth.models import User


class Post(BaseModel):
    DRAFT = 'DRAFT'
    PUBLISH = 'PUBLISH'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISH, 'Publish')
    )

    title = models.CharField(max_length=200, verbose_name='title')
    body = RichTextUploadingField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    reading_time = models.PositiveSmallIntegerField(verbose_name='reading time')
    slug = models.SlugField(max_length=200, verbose_name='slug')
    status = models.CharField(verbose_name='status', max_length=10, choices=STATUS_CHOICES)
    promote = models.BooleanField(verbose_name='promote', default=False)

    def __str__(self):
        return f"{self.author.username} - {self.title[:30]}"

    def get_absolute_url(self):
        return reverse(
            'post:post_detail',
            args=[self.author.id, self.slug]
        )

    def like_count(self):
        return self.post_vote.count()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'
        ordering = ('-created_time',)
