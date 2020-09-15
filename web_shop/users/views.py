from django.shortcuts import render, redirect
from . forms import UserRegisterForm, EmailChangeForm, DetailsChangeForm
from django.contrib.auth.decorators import login_required


def UserRegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
#-------------------------------------------------------------------------------

@login_required
def ProfileView(request):
    return render(request, 'users/profile.html')
#-------------------------------------------------------------------------------

@login_required
def EmailChangeView(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EmailChangeForm(instance=request.user)

    context = {'form':form}
    return render(request, 'users/email_change.html', context)
#-------------------------------------------------------------------------------

def DetailsChangeView(request):
    if request.method == 'POST':
        form = DetailsChangeForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DetailsChangeForm(instance=request.user.profile)

    context = {'form':form}
    return render(request, 'users/user_details_change.html', context)
