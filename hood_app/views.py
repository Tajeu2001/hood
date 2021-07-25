from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . forms import Registration
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import BusinessForm, UpdateProfileForm, NeighbourHoodForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Profile, Business, Post
from django.contrib import messages

# Create your views here.

#     def register(request):
#     if request.method == 'POST':
#         form = Registration(request.POST)
#         if form.is_valid():
#         form.save()
#         email = form.cleaned_data['email']
#         username = form.cleaned_data.get('username')

#         messages.success(request,f'Account for {username} created,you can now login')
#         return redirect('login')
#     else:
#         form = Registration()
#     return render(request,'registration/registration_form.html',{"form":form})

#     def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             messages.info(request, f"You are now logged in as {username}")
#             return redirect('index')
#         else:
#             messages.error(request, "Invalid username or password.")
#         else:
#         messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request = request,template_name = "registration/login.html",context={"form":form})

# @login_required
# def index(request):
#     all_hoods = Neighbourhood.objects.all()
#     all_hoods = all_hoods[::-1]
#     params = {
#         'all_hoods': all_hoods,
#     }
#     return render(request, 'index.html', params)



# def create_neighbourhood(request):
#     if request.method == 'POST':
#         form = NeighbourHoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hood = form.save(commit=False)
#             hood.admin = request.user.profile
#             hood.save()
#             return redirect('index')
#     else:
#         form = NeighbourHoodForm()
#     return render(request, 'newhood.html', {'form': form})


# def join_neighbourhood(request, id):
#     neighbourhood = get_object_or_404(Neighbourhood, id=id)
#     request.user.profile.neighbourhood = neighbourhood
#     request.user.profile.save()
#     return redirect('index')


# def leave_neighbourhood(request, id):
#     hood = get_object_or_404(Neighbourhood, id=id)
#     request.user.profile.neighbourhood = None
#     request.user.profile.save()
#     return redirect('index')

# def single_neighbourhood(request, hood_id):
#     hood = Neighbourhood.objects.get(id=hood_id)
#     business = Business.objects.filter(neighbourhood=hood)
#     posts = Post.objects.filter(hood=hood)
#     posts = posts[::-1]
#     if request.method == 'POST':
#         form = BusinessForm(request.POST)
#         if form.is_valid():
#             b_form = form.save(commit=False)
#             b_form.neighbourhood = hood
#             b_form.user = request.user.profile
#             b_form.save()
#             return redirect('single-hood', hood.id)
#     else:
#         form = BusinessForm()
#     params = {
#         'hood': hood,
#         'business': business,
#         'form': form,
#         'posts': posts
#     }
#     return render(request, 'single_hood.html', params)


# def create_post(request, hood_id):
#     hood = Neighbourhood.objects.get(id=hood_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.hood = hood
#             post.user = request.user.profile
#             post.save()
#             return redirect('single-hood', hood.id)
#     else:
#         form = PostForm()
#     return render(request, 'post.html', {'form': form})
