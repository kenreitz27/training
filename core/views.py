from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from core.forms import SignUpForm

# Create your views here.

def core_index(request):
  return render(request, 'core_index.html', {})

def core_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    context = {
      "form": form
    }
    return render(request, 'core_signup.html', context)
  
def core_login(request):
  return render(request, 'core_login.html', {})
