from django.urls import path
from . import views

app_name = 'activity'
urlpatterns = [
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('add_reply/<int:post_id>/<int:comment_id>/', views.add_reply, name='add_reply'),
    path('follow/', views.user_follow, name='follow'),
    path('unfollow/', views.user_unfollow, name='unfollow'),
    path('like/', views.post_like, name='like'),
    path('unlike/', views.post_unlike, name='unlike'),
]
