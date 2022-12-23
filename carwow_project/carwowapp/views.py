from django.shortcuts import render, redirect
from .models import Cars
from .forms import Carsform
from .forms import Carsform
# Create your views here.
def index(request):
    cars=Cars.objects.all()
    context={
        'cars_list':cars
    }
    return render(request,'index.html',context)
def details(request,cars_id):
    cars=Cars.objects.get(id=cars_id)
    return render(request,'details.html',{'cars':cars})
def add_car(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        price=request.POST.get('price',)
        img=request.FILES['img']
        cars=Cars(name=name,desc=desc,price=price,img=img)
        cars.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
   cars=Cars.objects.get(id=id)
   form=Carsform(request.POST or None,request.FILES,instance=cars)
   if form.is_valid():
       form.save()
       return redirect('/')
   return render(request, 'update.html',{'form':form,'cars':cars})
def delete(request,id):
    if request.method=='POST':
        cars=Cars.objects.get(id=id)
        cars.delete()
        return redirect('/')
    return render(request,'delete.html')





