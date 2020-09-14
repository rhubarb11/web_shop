from django.shortcuts import render, redirect
from . forms import UserRegisterForm
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
