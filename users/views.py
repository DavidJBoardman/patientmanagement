from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Handles user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # is valid uses django backend to check if users account already exists and meets requirements.
        if form.is_valid():
            # Automatically hashes password and saves user
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('mysite-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})