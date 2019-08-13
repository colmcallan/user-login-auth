from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.
def index(request):
    """Return index.html file"""
    return render(request, 'index.html')
    
def logout(request):
    """log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
    
def login(request):
    """Return Log in page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], 
                                     password=request.POST['password'])
            messages.success(request, "You have logged in succesfully!")
            
            if user:
                auth.login(user=user, request=request)
            else:
                login_form.add_error(None, "Your username or password is invalid")
        else:
            login_form = UserLoginForm()

    return render(request, 'login.html', {"login_form": login_form})
    


