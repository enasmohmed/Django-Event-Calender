from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic

from eventcalender.models import Event, EventMember
from .forms import UserForm, ProfileForm, SignupForm
from .models import Profile
from django.contrib.auth import get_user_model, update_session_auth_hash

from .tokens import confirmation_email_token_generator
from .utils import send_confirmation_email

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)
            return render(request, 'registration/signup_success.html')

    else:
        form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})





@login_required(login_url='/accounts/login/')
def profile_detail(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    all_event = Event.objects.filter(user=user)
    all_member = EventMember.objects.filter(user=user)
    context = {
        'user': user,
        'profile': profile,
        'all_event': all_event,
        'all_member': all_member
    }
    return render(request, 'registration/profile.html', context)


# edit profile
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile_detail'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'registration/edit_profile.html',{'userform':userform , 'profileform':profileform})

# confirmation email
def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirmation_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('accounts:login')

    else:
        return HttpResponseBadRequest('Bad Token')


# change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:profile_detail')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })