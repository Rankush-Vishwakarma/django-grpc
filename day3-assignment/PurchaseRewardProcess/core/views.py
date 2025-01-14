from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

# Create your views here.
def signup(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    validator_Node = request.POST.get('validator_Node')
    party_Id = request.POST.get('party_Id')
    threshold = request.POST.get('threshold')
    #user = User.objects.create_user(name=name, email=email)
    try:
      # checking if the same user is present in the node if it is present then jsut skip to login
      user_profile = UserProfile.objects.get(name = name, email=email, validator_Node=validator_Node)
      login(request,user_profile)
      messages.success(request, 'User logged in successfully')
      return redirect('trafficpurchase')
    except UserProfile.DoesNotExist:
      user_profile = UserProfile.objects.create(
        name=name,
        email=email,
        validator_Node=validator_Node,
        party_Id=party_Id,
        threshold=threshold,
        current_Balance=0
      )
      user_profile.save()
      messages.success(request, 'User created successfully')
      return redirect('trafficpurchase')
  return render(request, 'core/signup.html')

def index(request):
  return redirect('signup')
