from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView,UpdateView

from event.models import Event
from .forms import SignUpForm, ProfileForm
from .models import Profile
from .tokens import confirmation_email_token_generator
from .utils import send_confirmation_email
from django.contrib.auth import get_user_model


User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request,user)
            return render(request, 'registration/signup_success.html')

    else:
        form = SignUpForm
    return render(request, 'registration/signup.html', {'form': form})



def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirmation_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('accounts:login')

    else:
        return HttpResponseBadRequest('Bad Token')




@login_required(login_url='/accounts/login/')
def profile_detail(request):
    user = request.user
    context = {
        'user' : user ,
    }
    return render(request , 'registration/profile.html' , context)






def edit_profile(request):
    user = request.user
    form = ProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
    if request.method == 'POST':
        if form.is_valid():
            user.save()
            return HttpResponseRedirect('%s'%(reverse('profile')))

    context = {
        "form": form
    }

    return render(request, "registration/edit_profile.html", context)

