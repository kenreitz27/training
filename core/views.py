from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from core.forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Create your views here.

def core_index(request):
  return render(request, 'core_index.html', {})

def core_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core_index') # changed from '/'
    else:
        form = SignUpForm()
    context = {
      "form": form
    }
    return render(request, 'core_signup.html', context)
  
def core_login(request):
  return render(request, 'core_login.html', {})

@login_required
@transaction.atomic
def core_profile(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, _('Your profile was successfully updated!'))
      return redirect('settings:profile')
    else:
      messages.error(request, _('Please correct the error below.'))
  else:
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
  
  return render(request, 'core_profile_edit.html', {
    'user_form': user_form,
    'profile_form': profile_form
    })

