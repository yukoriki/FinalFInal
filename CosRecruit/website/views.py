from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import AddRecordForm
from .models import Record

#HOME VIEW
def home(request):
    records = Record.objects.all()

    #LOGIN CONFIRMATION
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']

        #AUTHENTICATION
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.success(request, "Login Failed. Did you enter the right credentials?")
            return redirect('home')
        
    else: 
        return render (request, 'home.html', {'records':records})
#LOGIN
def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out. See you next time!")
    return redirect('home')

#REGISTER
def register_user(request):
    if request.method == "POST": 
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #AUTHENTICATION
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Register Successful, Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()

    return render (request, 'register.html', {'form': form})

#RECORDS
def applicant_record(request, pk):
    if request.user.is_authenticated:
        applicant_record = Record.objects.get(id=pk)
        return render (request, 'record.html', {'applicant_record': applicant_record})
    
    else:
        messages.success(request, "Uh oh! you need to be logged in to view this page!")
        return redirect('home')
    
#DELETE
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Details deleted. Sorry to see this one go..")
        return redirect('home')
    else:
        messages.success(request, "Uh oh! you need to be logged in to do that!")
        return redirect('home')
    
#ADD
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Applicant Added! Thank you!")
                return redirect('home')
        return render (request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Uh oh! you need to be logged in to do that!")
        return redirect('home')
    
#UPDATE   
def update_record(request,pk): 
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
                form.save()
                messages.success(request, "Applicant details updated! WooHoo!")
                return redirect('home')
        return render (request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Uh oh! you need to be logged in to do that!")
        return redirect('home')