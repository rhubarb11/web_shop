from django.shortcuts import render, redirect
from . forms import UserRegisterForm


def UserRegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
        form = {'form': form, 'title': 'register'}
    return render(request, 'users/register.html', form)
