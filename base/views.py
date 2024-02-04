from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def Wardrobe(request):
    img = Image.objects.all()
    return render(request,'index.html',{'img':img})

def add_clothes(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()    
    return render(request,'add_cloth.html',{'form':form})