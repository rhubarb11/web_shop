from django.shortcuts import render, redirect
from . forms import UserRegisterForm, EmailChangeForm, DetailsChangeForm, CustomAuthForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy


def userRegisterView(request):
    if request.user.is_authenticated:
        return redirect('shop-index')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration completed. You can now sign in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
#-------------------------------------------------------------------------------

@login_required
def userInfoView(request):
    return render(request, 'users/user.html')
#-------------------------------------------------------------------------------

@login_required
def emailChangeView(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your email has been changed')
            return redirect('user')
    else:
        form = EmailChangeForm(instance=request.user)

    context = {'form':form}
    return render(request, 'users/email_change.html', context)
#-------------------------------------------------------------------------------

@login_required
def detailsChangeView(request):
    if request.method == 'POST':
        form = DetailsChangeForm(request.POST, instance=request.user.userdetails)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your details updated')
            return redirect('user')
    else:
        form = DetailsChangeForm(instance=request.user.userdetails)

    context = {'form':form}
    return render(request, 'users/user_details_change.html', context)

#-------------------------------------------------------------------------------

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('user')

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed')
        return super().form_valid(form)
