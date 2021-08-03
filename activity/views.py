from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from post.models import Post
from .models import Comment, Relation, Vote
from .forms import AddCommentForm, AddReplyForm


@login_required()
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'Your comment submitted successfully.', 'success')
            return redirect(
                'post:post_detail', request.user.id, post.created_time.year, post.created_time.month,
                post.created_time.day, post.slug
            )


@login_required
def add_reply(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = AddReplyForm(request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.user = request.user
            new_reply.post = post
            new_reply.reply = comment
            new_reply.is_reply = True
            new_reply.save()
            messages.success(request, 'Your reply submitted successfully', 'success')
            return redirect(
                'post:post_detail', request.user.id, post.created_time.year, post.created_time.month,
                post.created_time.day, post.slug
            )


@login_required
def user_follow(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        following = get_object_or_404(User, pk=user_id)
        check_relation = Relation.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            return JsonResponse({'status': 'exists'})
        else:
            Relation(from_user=request.user, to_user=following).save()
            return JsonResponse({'status': 'ok'})


@login_required
def user_unfollow(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        following = get_object_or_404(User, pk=user_id)
        check_relation = Relation.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            check_relation.delete()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'not_exist'})


@login_required
def post_like(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = get_object_or_404(Post, pk=post_id)
        check_vote = Vote.objects.filter(user=request.user, post=post)
        if check_vote.exists():
            return JsonResponse({'status': 'exists'})
        else:
            Vote(user=request.user, post=post).save()
            return JsonResponse({'status': 'ok', 'like_count': post.like_count()})


@login_required
def post_unlike(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = get_object_or_404(Post, pk=post_id)
        check_vote = Vote.objects.filter(user=request.user, post=post)
        if check_vote.exists():
            check_vote.delete()
            return JsonResponse({'status': 'ok', 'like_count': post.like_count()})
        else:
            return JsonResponse({'status': 'not_exist'})
