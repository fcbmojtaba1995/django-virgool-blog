from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post
from .forms import AddPostForm, EditPostForm
from activity.forms import AddCommentForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from activity.models import Comment, Vote
from redis import Redis
from virgool.local_settings import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD


def all_posts(request):
    posts = Post.objects.filter(status=Post.PUBLISH)
    return render(request, 'post/all_posts.html', context={'posts': posts})


redis_connection = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)


def post_detail(request, user_id, slug):
    if request.user.id == user_id:
        post = get_object_or_404(Post, slug=slug)
    else:
        post = get_object_or_404(Post, status=Post.PUBLISH, slug=slug)
    comments = Comment.objects.filter(post=post, is_reply=False)
    form = AddCommentForm()
    redis_connection.hsetnx('post_views', post.id, 0)
    post_views = redis_connection.hincrby('post_views', post.id)
    is_like = False
    if request.user.is_authenticated:
        vote = Vote.objects.filter(user=request.user, post=post)
        if vote.exists():
            is_like = True
    return render(
        request, 'post/post_detail.html',
        context={'post': post, 'comments': comments, 'is_like': is_like, 'post_views': post_views, 'form': form}
    )


@login_required
def add_post(request, user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.slug = slugify(form.cleaned_data['title'][:40], allow_unicode=True)
                new_post.save()
                messages.success(request, 'Your post submitted successfully', 'success')
                return redirect('account:dashboard', user_id)
        else:
            form = AddPostForm()
        return render(request, 'post/add_post.html', context={'form': form})
    else:
        return HttpResponse('Access denied')


@login_required
def edit_post(request, user_id, post_id):
    if request.user.id == user_id:
        post = get_object_or_404(Post, pk=post_id)
        if request.method == 'POST':
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                ep = form.save(commit=False)
                ep.slug = slugify(form.cleaned_data['title'][:40], allow_unicode=True)
                ep.save()
                messages.success(request, 'Your post edited successfully', 'success')
                return redirect('account:dashboard', user_id)
        else:
            form = EditPostForm(instance=post)
        return render(request, 'post/edit_post.html', context={'form': form, 'post_id': post_id})
    else:
        return HttpResponse('Access Denied')


@login_required
def delete_post(request, user_id, post_id):
    if request.user.id == user_id:
        Post.objects.filter(pk=post_id).delete()
        messages.success(request, 'your post deleted successfully', 'success')
        return redirect('account:dashboard', user_id)
    else:
        return HttpResponse('Access denied')
