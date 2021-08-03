from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, UserEditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from post.models import Post
from activity.models import Relation


def user_login(request):
    if request.method == 'POST':
        next_url = request.POST.get("next", False)
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')

                if next_url:
                    return redirect(next_url)

                return redirect('home:home')
            else:
                messages.error(request, 'Wrong username or password', 'error')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', context={'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            login(request, user)
            messages.success(request, 'You register successfully', 'success')
            return redirect('home:home')

    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('home:home')


@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=user)
    is_following = False
    relation = Relation.objects.filter(from_user=request.user, to_user=user)
    if relation.exists():
        is_following = True
    return render(
        request, 'account/dashboard.html', context={'user': user, 'posts': posts, 'is_following': is_following}
    )


@login_required
def user_edit_profile(request, user_id):
    profile = Profile.objects.get(user_id=user_id)

    if request.method == 'POST':
        form = UserEditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            user = User.objects.filter(username__exact=username)
            if user.exists() and request.user.username != username:
                messages.error(request, 'Username has already taken by someone else', 'warning')
            else:
                profile.user.username = username
                profile.user.first_name = cleaned_data['first_name']
                profile.user.last_name = cleaned_data['last_name']
                profile.user.email = cleaned_data['email']
                profile.user.save()
                messages.success(request, 'your profile edited successfully', 'success')
                return redirect('account:dashboard', user_id)
    else:
        form = UserEditProfileForm(
            instance=profile,
            initial={
                'username': request.user.username, 'first_name': request.user.first_name,
                'last_name': request.user.last_name, 'email': request.user.email
            }
        )
    return render(request, 'account/edit_profile.html', context={'form': form})


@login_required
def user_delete_account(request, user_id):
    if user_id == request.user.id:
        User.objects.filter(id=user_id).delete()
        messages.success(request, 'Your account has been deleted', 'success')
        return redirect('home:home')
    else:
        return redirect('home:home')
