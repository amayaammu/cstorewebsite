from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from dstoreapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from dstoreapp.models import cartdb, checkoutdb, chemicaldb, registerdb
# Create your views here.
def index(request):
    ucount=storedb.objects.all().count()
    ucount1=productdb.objects.all().count()
    ucount2=registerdb.objects.all().count()
    ucount3=chemicaldb.objects.all().count()
    ucount4=checkoutdb.objects.all().count()
    return render(request,'index.html',{'ucount':ucount,'ucount1':ucount1,'ucount2':ucount2,'ucount3':ucount3,'ucount4':ucount4})
    

def add_category(request):
    return render(request,'add_category.html')

def view_category(request):
    data = storedb.objects.all()
    return render(request,'view_category.html',{'data':data})

def getdata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        image=request.FILES['image']
        data=storedb(name=name,description=description,image=image)
        data.save()
    return redirect('view_category')

def edit(request,trid):
    data = storedb.objects.filter(id=trid)
    return render(request,'edit.html',{'data':data})
    
def update(request,uid):
    if request.method == 'POST':
       name_c = request.POST.get('name')
       description_c = request.POST.get('description')
    storedb.objects.filter(id=uid).update(name=name_c,description=description_c)
    try:
        image_r=request.FILES['image']
        fs = FileSystemStorage() 
        file = fs.save(image_r.name, image_r)
    except MultiValueDictKeyError :
        file=storedb.objects.get(id=uid).image
    storedb.objects.filter(id=uid).update(name=name_c,description=description_c,image=file)
    return redirect('view_category')
def delete(request,did):
    storedb.objects.get(id=did).delete()
    return redirect('view_category')

def add_product(request):
    data = storedb.objects.all()
    return render(request,'add_product.html',{'data':data})

def view_product(request):
    data = productdb.objects.all()
    return render(request,'view_product.html',{'data':data})

def getpro(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        weight=request.POST.get('weight')
        price=request.POST.get('price')
        image=request.FILES['image']
        data=productdb(pname=pname,weight=weight,price=price,image=image)
        data.save()
    return redirect('view_product')

def edit1(request,eid):
    data = productdb.objects.filter(id=eid)
    return render(request,'edit1.html',{'data':data})
    
def update1(request,pid):
    if request.method == 'POST':
       pname_c = request.POST.get('pname')
       weight_c = request.POST.get('weight')
       price_c = request.POST.get('price')
    productdb.objects.filter(id=pid).update(pname=pname_c,weight=weight_c,price=price_c)
    try:
        image_r=request.FILES['image']
        fs = FileSystemStorage() 
        file = fs.save(image_r.name, image_r)
    except MultiValueDictKeyError :
        file=productdb.objects.get(id=pid).image
    productdb.objects.filter(id=pid).update(pname=pname_c,weight=weight_c,price=price_c,image=file)
    return redirect('view_product')
def delete1(request,lid):
    productdb.objects.get(id=lid).delete()
    return redirect('view_product')

def adminlogin(request):
    return render(request,'adminlogin.html')

def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('index')
        else:
            return render(request,'adminlogin.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('adminlogin')


    
