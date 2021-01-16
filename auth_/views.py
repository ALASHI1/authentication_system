from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
 
# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'acc/dashboard.html',{'section': 'dashboard'})

def homepage(request):
    return render(request, 'acc/homepage.html',{})




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password']) # Save the User object
            new_user.save()
            return render(request,'acc/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'acc/register.html',{'user_form': user_form})
