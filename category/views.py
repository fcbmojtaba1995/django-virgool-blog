from django.shortcuts import render
from .models import Category
from post.models import Post


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'category/all_categories.html', context={'categories': categories})


def posts_in_category(request, category_id, category_name):
    posts = Post.objects.filter(category=category_id)
    category_info = {
        'name': category_name,
        'posts_count': posts.count()
    }
    return render(request, 'category/posts_in_category.html', context={'category': category_info, 'posts': posts})
