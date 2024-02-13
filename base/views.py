from django.shortcuts import render , redirect
from .forms import ImageForm , CustomUserCreationForm
from .models import Image
from  django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .forms import CustomUserCreationForm

# Create your views here.
def loginPage(request):
    page ='login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request , username=username,password = password)

        if user is not None:
            login(request,user)
            return redirect('Wardrobe')
    return render(request,'login_register.html',{'page':page})

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = CustomUserCreationForm()
    page = 'register'

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

        user = authenticate(request , username=user.username,password = request.POST['password1'])

        if user is not None:
            login(request ,user)
            return redirect('Wardrobe')
            
    context={'form':form, 'page':page}
    return render(request,'login_register.html',context)


@login_required(login_url='login')
def Wardrobe(request):
    Current_user = request.user
    img = Image.objects.filter(user = Current_user)
    return render(request,'index.html',{'img':img})


# @login_required(login_url='login')
# def add_clothes(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()   
#     form = ImageForm()    
#     return render(request,'add_cloth.html',{'form':form})
@login_required(login_url='login')
def add_clothes(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the current user as the value for the user field
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Clothes added successfully!')
            # Redirect or render success page
        else:
            messages.error(request, 'Form submission failed. Please correct the errors.')    
    else:
        # Pass the current user as initial data to the form
        form = ImageForm(initial={'user': request.user})
    Current_user = request.user
    img = Image.objects.filter(user = Current_user)
    
    context={'form':form, 'img':img}    
    return render(request, 'add_cloth.html', context)