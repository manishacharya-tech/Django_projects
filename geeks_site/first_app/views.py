from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import first_app.models
from first_app.forms import FormName, UserProfile,UserForm
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    access_records = first_app.models.AccessRecord.objects.order_by('date')
    my_dict = {'access_records' : access_records }
    return render(request, 'first_html/index.html', context=my_dict)

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

# def user(request):
#     users = first_app.models.User.objects.all()
#     user_dict = {'users' : users}
#     return render(request, 'first_html/user.html',context=user_dict)

def Form(request):
    Form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
    return render(request, 'first_html/form_page.html',{'form' : Form})

# def Userform(request):
#     user = Userf()
#     print(request.method)
#     if request.method == 'POST':
#         form = Userf(request.POST)
#         if form.is_valid():
#             print('email:' + form.cleaned_data['email'])
#             form.save(commit=True)
#             print('data saved')
#             return index(request)
#         else:
#             print('error form is not valid')
#     return render(request, 'first_html/user.html', {'user': user})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfile(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfile()

    return render(request,'first_html/user.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'first_html/login.html', {})
