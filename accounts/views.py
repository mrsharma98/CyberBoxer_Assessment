from django.shortcuts import render, redirect
from .forms import UserForm,UserProfileInfoForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

            return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'error':user_form.errors})
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'accounts/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # this will try for the authentication, if it does authenticate
        # it will give us a valid user object
        if user is not None:
            # if we do get a user object
            login(request, user)
            request.session['username'] = user.username

            return redirect('/')

        else:
            # if the user is None
            return render(request, 'accounts/login.html', {'error':'Username or passowrd is incorrect'})

    else:
        return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    if request.method == "POST":
        del request.session['username']
        logout(request)

        return redirect('login')

    return render(request, 'accounts/signup.html')
