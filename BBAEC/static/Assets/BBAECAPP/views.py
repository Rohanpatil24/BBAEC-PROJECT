from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from BBAECAPP.models import banquet,menu,dishes,menucart,foodcart
from django.contrib.auth import authenticate,login,logout
import random
from django.db.models import Q

# Create your views here.

def Home(request):
    userid=request.user.id
    username=request.user.username
    print(userid,username)
    context={}
    b=banquet.objects.filter(is_active=True)
    context['Banquets']=b   
    d=dishes.objects.filter(is_active=True)
    context['dishes']=d

    indian=dishes.objects.filter(mid=1)
    context['indveg']=indian

    chinese=dishes.objects.filter(mid=2)
    context['chinese']=chinese

    Continental=dishes.objects.filter(mid=3)
    context['continental']=Continental

    indnonveg=dishes.objects.filter(mid=4)
    context['indnonveg']=indnonveg

    MaharastrianAgriKoli=dishes.objects.filter(mid=5)
    context['MaharastrianAgriKoli']=MaharastrianAgriKoli

    Malvani=dishes.objects.filter(mid=6)
    context['Malvani']=Malvani
    
    SouthIndian=dishes.objects.filter(mid=7)
    context['SouthIndian']=SouthIndian

    Rajastani=dishes.objects.filter(mid=8)
    context['Rajastani']=Rajastani     

    return render(request,'home.html',context)
    

# def TopB(request):
#     banq=banquet.objects.filter(is_active=True)
#     context={}
#     context['banq']=banq
#     for i in banq:
#         print(i.name)
#     return render(request,'home.html')

def Login(request):
    if request.method == 'POST':
        UEmail=request.POST['email']
        UPassword=request.POST['password']
        print(UEmail,UPassword)
        context={}
        if UEmail=="" or UPassword=='':
            context['logerror']="Please fill all the required data, this fields cannot be empty!!"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=UEmail,password=UPassword)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context['logerror']="Invalid Username or Password"
                return render(request,'login.html',context)
    else:
        return render(request,'login.html')


def Registration(request):
    if request.method == 'POST':
        UFname=request.POST['fname']
        ULname=request.POST['lname']
        UEmail=request.POST['email']
        UPassword=request.POST['password']
        UCPassword=request.POST['confirmpassword']
        print(UFname,ULname,UEmail,UPassword,UCPassword)
        context={}
        if UEmail=="" or UPassword=='' or UCPassword =='':
            context['regerror']="Please fill all the required data, this fields cannot be empty!!"
            return render(request,'registration.html',context)
        elif UPassword != UCPassword:
            context['regerror']="Password doesn't match both password must be same"
            return render(request,'registration.html',context)
        else:
            try:
                u=User.objects.create_user(
                password=UPassword,username=UEmail,first_name=UFname,last_name=ULname,
                email=UEmail
                )
                u.set_password(UPassword)
                u.save()
                context={}
                context['successful']="Registration Complete"
                return render(request,'registration.html',context)
            except Exception:
                context['regerror']="Username is already regisered try different username"
                return render(request,'registration.html',context)
    else:
        return render(request,'registration.html')



def ulogout(request):
    logout(request)
    return redirect('/home')

def Preview(request,bid):
    b=banquet.objects.filter(id=bid)
    context={}
    context['Banquets']=b

    indian=dishes.objects.filter(mid=1)
    context['indveg']=indian

    chinese=dishes.objects.filter(mid=2)
    context['chinese']=chinese

    Continental=dishes.objects.filter(mid=3)
    context['continental']=Continental

    indnonveg=dishes.objects.filter(mid=4)
    context['indnonveg']=indnonveg

    MaharastrianAgriKoli=dishes.objects.filter(mid=5)
    context['MaharastrianAgriKoli']=MaharastrianAgriKoli

    Malvani=dishes.objects.filter(mid=6)
    context['Malvani']=Malvani
    
    SouthIndian=dishes.objects.filter(mid=7)
    context['SouthIndian']=SouthIndian

    Rajastani=dishes.objects.filter(mid=8)
    context['Rajastani']=Rajastani 

    m=menu.objects.filter(is_active=True)
    context['menu']=m


    return render(request,'preview.html',context)

def fooddata(request,mid):
    if request.user.is_authenticated:      
        userid=request.user.id
        u=User.objects.filter(id=userid)
        print(u)
        m=menu.objects.filter(id=mid)
        print(m)
        q1=Q(userid=u[0])
        q2=Q(menuid=m[0])
        c=foodcart.objects.filter(q1 & q2)
        n=len(c)
        print(n)
        context={}
        context['Menu']=m
        if n==1:
            context['msg']="Product exits already in cart!!!"
            return render(request,'preview.html',context)
        else:
            c=foodcart.objects.create(userid=u[0],menuid=m[0])
            c.save()
            context={}
            context['success']="Menu Added to cart"
            context['products']=m
            return render(request,'preview.html',context)
    else:
        return redirect('/login')


def addtocart(request,bid):
    if request.user.is_authenticated:      
        userid=request.user.id
        u=User.objects.filter(id=userid)
        print(u)
        b=banquet.objects.filter(id=bid)
        print(b)
        q1=Q(userid=u[0])
        q2=Q(banqid=b[0])
        c=menucart.objects.filter(q1 & q2)
        n=len(c)
        print(n)
        context={}
        context['banquet']=b
        if n==1:
            context['msg']="Product exits already in cart!!!"
            return render(request,'preview.html',context)
        else:
            c=menucart.objects.create(userid=u[0],banqid=b[0])
            c.save()
            context={}
            context['success']="Product Added to cart"
            context['products']=b
            return render(request,'preview.html',context)
    else:
        return redirect('/login')



def cart(request):
    c=menucart.objects.filter(userid=request.user.id)
    d=foodcart.objects.filter(userid=request.user.id)
    s=0
    m=0
    for x in c:
        s=s+x.banqid.rent*x.qty
    for y in d:
        m=m+y.menuid.package*y.qty
    np=len(c)
    context={}
    context['items']=np
    context['total']=s+m
    context['data']=c
    context['menu']=d
    return render(request, 'cart.html',context)

def remove(request,uid):
    c=menucart.objects.filter(id=uid)
    c=c.delete()
    return redirect('/cart')

def menuremove(request,uid):
    c=foodcart.objects.filter(id=uid)
    c=c.delete()
    return redirect('/cart')

def updateqty(request,qv,menuid):
    d=foodcart.objects.filter(id=menuid)
    if qv=='1':
        t=d[0].qty+1
        d.update(qty=t)
    else:
        if d[0].qty>1:
            t=d[0].qty-1
            d.update(qty=t)
    return redirect('/cart')


# def placeorder(request):
#     userid=request.user.id
#     c=menucart.objects.filter(userid=request.user.id)
#     d=foodcart.objects.filter(userid=request.user.id)
#     #print(c)
#     oid=random.randrange(1000,9999)
#     print(oid)
#     for x in c:
#         o=Order.objects.create(order_id=oid,bid=x.banqid,uid=x.userid,mid=x.banqid,qty=x.qty)
#         o.save()
#         x.delete()
#     orders=Order.objects.filter(uid=userid)
#     context={}
#     context['data']=orders
#     s=0
#     m=0
#     for x in orders:
#         s=s+x.bid.rent*x.qty
#     for y in d:
#         s=s+y.menuid.package*y.qty
    
#     np=len(orders)
#     context['items']=np
#     context['total']=s+m
#     return render(request, 'placeorder.html',context)




