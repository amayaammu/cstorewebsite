from django.shortcuts import render,redirect
from django.http import HttpResponse
from cstoreapp. models import *
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def indexa(request):
    data=storedb.objects.all()
    return render(request,'indexa.html',{'data':data})

def about1(request):
    return render(request,'about.html')

def contact1(request):
    return render(request,'contact1.html')

def contacttable(request):
    data=chemicaldb.objects.all()
    return render(request,'contacttable.html',{'data':data})

def getstore(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('phone')
        message=request.POST.get('message')
        data=chemicaldb(name=name,phone=phone,email=email,message=message)
        data.save()
    return redirect('indexa')

def register1(request):
    return render(request,'register1.html')



def regi1(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        phone=request.POST.get('phone')
        uname=request.POST.get('username')
        password=request.POST.get('password')
        data=registerdb(name=name,phone=phone,uname=uname,password=password)
        data.save()
    return redirect('indexa')

def registration(request):
    data=registerdb.objects.all()
    return render(request,'registration.html',{'data':data})

def userlogin1(request):
    return render(request,'userlogin.html')

def userin1(request):
    uname = request.POST.get('username')
    password = request.POST.get('password')
    print(uname)
    print(password)
    if registerdb.objects.filter(uname=uname,password=password).exists():
        data = registerdb.objects.filter(uname=uname,password=password).values('name','phone','id').first()
        request.session['name'] =data['name']
        request.session['phone'] = data['phone']
        request.session['uname'] = uname
        request.session['password'] = password
        request.session['id'] = data['id']
        return redirect('indexa')

def logout1(request):
    del request.session['name']
    del request.session['phone']
    del request.session['uname']
    del request.session['password']
    del request.session['id']
    return redirect('indexa')

def products(request):
    data=productdb.objects.all()
    return render(request,'products.html',{'data':data})

def single(request,pid):
    data=productdb.objects.filter(id=pid)
    return render(request,'single.html',{'data':data})

def cart(request):
    u = request.session.get('id')
    data=cartdb.objects.filter(userid=u,status=0)
    total = cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'total':total})

def checkout(request):
    u = request.session.get('id')
    data=cartdb.objects.filter(userid=u,status=0)
    total = cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'checkout.html',{'data':data,'total':total})

def cart1(request,pid):
    if request.method=="POST":
        userid=request.POST.get('userid')
        total=request.POST.get('total')
        quantity=request.POST.get('quantity')
        data=cartdb(productid=productdb.objects.get(id=pid),userid=registerdb.objects.get(id=userid),total=total,quantity=quantity,status=0)
        data.save()
    return redirect('cart')

def deletec(request,cid):
    data=cartdb.objects.filter(id=cid).delete()
    return redirect('cart')

def checkout1(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        u = request.session.get('id')
        order = cartdb.objects.filter(userid=u,status=0)
        for i in order:
            data = checkoutdb(cartid=cartdb.objects.get(id=i.id),name=name,email=email,mobile=mobile,address=address)
            data.save()
            cartdb.objects.filter(id=i.id).update(status=1)
    return redirect('indexa')

@csrf_exempt
def cart_update(request):
    if request.method == "POST":
        cartid = request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        cartdb.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()

def orders(request):
    data = checkoutdb.objects.all()
    return render(request,'orders.html',{'data':data})

def getorder(request):
    if request.method=="POST":
        cartid=request.POST.get('cartid')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        data=checkoutdb(cartid=cartid,name=name,email=email,mobile=mobile,address=address)
        data.save()
    return redirect('orders')




 



