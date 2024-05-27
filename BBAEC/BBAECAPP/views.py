from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from BBAECAPP.models import banquet,menu,dishes,bkcart,order,morder,manager,rating
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.db.models import Q
import random 
import razorpay

# Create your views here.


def register(request):
    if request.method == 'POST':
        ufname = request.POST['fname']
        ulname = request.POST['lname']
        uemail = request.POST['email']
        upassword = request.POST['password']
        uconfirmpassword = request.POST['confirmpassword']
        context={}
        if uemail=="" or upassword=="" or uconfirmpassword=="":
            context['regerror']="Field cannot be empty"
            return render(request,'register.html',context)
        elif upassword!=uconfirmpassword:
            context['regerror']="Password doesn't match both password must be same"
            return render(request,'register.html',context)
        else:
            try:
                u=User.objects.create_user(password=upassword,username=uemail,first_name=ufname,last_name=ulname,email=uemail)
                u.set_password(upassword)
                u.save()
                context['success']="User Register Successfully !! Login Now"
                return render(request,'register.html',context)
            except Exception:
                context['regerror']="Username is already regisered try different username"
                return render(request,'register.html',context)

        print(ufname,ulname,uemail,upassword,uconfirmpassword)
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        uemail=request.POST['email']
        upassword=request.POST['password']
        print(uemail,upassword)
        context={}
        if uemail=="" or upassword=="":
            context['loginerror']="Field cannot be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uemail,password=upassword)
            if u is not None:
                auth_login(request,u) 
                return redirect('/home')
            else:
                context={'loginerror':"Invalid Username or Password"}
                return render(request,'login.html',context)
    else:
        return render(request, 'login.html')

def forgotpassword(request,uid):
    if request.method=='POST':
        uemail=request.POST['email']
        upassword=request.POST['password']
        u=User.objects.filter(id=uid)
        u.delete()
        u=User.objects.create(password=upassword)
        u.save()
        context={}
        context['user']=u
        context['success']="Password Changed Successfully"
    return render(request,'forgotpassword.html',context)

def banquets(request):
    context={}
    b=banquet.objects.filter(is_active=True)
    context['Banquets']=b
    

    return render(request,'banquets.html',context)

def ulogout(request):
    logout(request)
    return redirect('/home')

def home(request):
    userid=request.user.id
    username=request.user.username
    
    context={}
    b=banquet.objects.filter(is_active=True)
    context['Banquets']=b
    print(b)

    rfive=banquet.objects.filter(rating=5)
    context['rfive']=rfive

    indveg=dishes.objects.filter(mid=1)
    context['indveg']=indveg

    indnonveg=dishes.objects.filter(mid=2)
    context['indnonveg']=indnonveg

    chinese=dishes.objects.filter(mid=3)
    context['chinese']=chinese

    continental=dishes.objects.filter(mid=4 )
    context['continental']=continental

    MaharastrianAgriKoli=dishes.objects.filter(mid=5 )
    context['MaharastrianAgriKoli']=MaharastrianAgriKoli

    Malvani=dishes.objects.filter(mid=6 )
    context['Malvani']=Malvani

    SouthIndian=dishes.objects.filter(mid=7 )
    context['SouthIndian']=SouthIndian

    Rajastani=dishes.objects.filter(mid=8 )
    context['Rajastani']=Rajastani
    
    return render(request,'index.html',context)

def banqpreview(request,bid):
    b=banquet.objects.filter(id=bid)
    context={}
    context['Banquet']=b
    
    m=manager.objects.filter(id=bid)
    context['Manager']=m
    print(m)

    m=menu.objects.filter(is_active=True)
    context['Menu']=m

    indveg=dishes.objects.filter(mid=1)
    context['indveg']=indveg

    indnonveg=dishes.objects.filter(mid=2)
    context['indnonveg']=indnonveg

    chinese=dishes.objects.filter(mid=3)
    context['chinese']=chinese

    continental=dishes.objects.filter(mid=4 )
    context['continental']=continental

    MaharastrianAgriKoli=dishes.objects.filter(mid=5 )
    context['MaharastrianAgriKoli']=MaharastrianAgriKoli

    Malvani=dishes.objects.filter(mid=6 )
    context['Malvani']=Malvani

    SouthIndian=dishes.objects.filter(mid=7 )
    context['SouthIndian']=SouthIndian

    Rajastani=dishes.objects.filter(mid=8 )
    context['Rajastani']=Rajastani

    return render(request,'preview.html',context)

def bbanqcart(request,bid):
    if request.user.is_authenticated:
        uid=request.user.id
        u=User.objects.filter(id=uid)
        b=banquet.objects.filter(id=bid)
        q1=Q(uid=u[0])
        q2=Q(bid=b[0])
        c=order.objects.filter(q1 & q2)
        n=len(c)
        context={}
        context['Banquet']=b
        if n==1:
            context['msg']="Banquet exists already in cart!!!"
            return render(request,'preview.html',context)
        else:
            c=order.objects.create(uid=u[0],bid=b[0])
            c.save()
            context={}
            context['success']="Product Added to cart"
            context['products']=c
            return redirect('/cart')
    else:
        return redirect('/login')


def mmenucart(request,mid):
    if request.user.is_authenticated:
        uid=request.user.id
        username=request.user.username
        u=User.objects.filter(id=uid)
        m=menu.objects.filter(id=mid)
        q1=Q(uid=u[0])
        q2=Q(mid=m[0])
        c=order.objects.filter(q1 & q2)
        n=len(c)
        print(n)
        context={}
        context['Menu']=m
        if n==1:
            context['msg']="Menu exits already in cart!!!"
            return render (request,'confirmmenu.html',context)
            #return HttpResponse("<h1>Menu exits already in cart!!!</h1>")
        else:
            c=order.objects.create(uid=u[0],mid=m[0])
            c.save()
            context={}
            context['success']="Menu Added to cart"
            context['Menu']=c
            return render(request,'confirmmenu.html',context)
            #return HttpResponse("<h1>Menu exits already in cart!!!</h1>")
    else:
        return redirect('/login')



def cart(request):
    userid=request.user.id
    context={}
    indveg=dishes.objects.filter(mid=1)
    context['indveg']=indveg

    indnonveg=dishes.objects.filter(mid=2)
    context['indnonveg']=indnonveg

    chinese=dishes.objects.filter(mid=3)
    context['chinese']=chinese

    continental=dishes.objects.filter(mid=4 )
    context['continental']=continental

    MaharastrianAgriKoli=dishes.objects.filter(mid=5 )
    context['MaharastrianAgriKoli']=MaharastrianAgriKoli

    Malvani=dishes.objects.filter(mid=6 )
    context['Malvani']=Malvani

    SouthIndian=dishes.objects.filter(mid=7 )
    context['SouthIndian']=SouthIndian

    Rajastani=dishes.objects.filter(mid=8 )
    context['Rajastani']=Rajastani

    oc=order.objects.filter(uid=request.user.id)
    c=0
    b=0
    m=0
    booking=999
    for x in oc:
        print(x)
        b=b+x.bid.rent*x.qty
        m=m+x.mid.package*x.qty
    np=len(oc)
    context={}
    context['data']=oc
    context['items']=np
    context['total']=m+b
    context['booktotal']=booking

    return render(request,'cart.html',context)


def placeorder(request):
    userid=request.user.id
    c=order.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)

    for x in c:
        o=morder.objects.create(order_id=oid,
                               qty=x.qty,mid=x.mid,uid=x.uid,bid=x.bid,)
        o.save()
        x.delete()
    orders=morder.objects.filter(uid=userid)
    context={}
    context['data']=orders
    b=0
    m=0
    for x in orders:
        m=m+x.mid.package*x.qty
        b=b+x.bid.rent*x.qty
    np=len(orders)
    
    context['items']=np
    context['total']=m+b
    return render(request, 'placeorder.html',context)

def bkplaceorder(request):
    userid=request.user.id
    c=order.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)

    for x in c:
        o=bkcart.objects.create(order_id=oid,
                               qty=x.qty,mid=x.mid,uid=x.uid,bid=x.bid,)
        o.save()
        x.delete()
    orders=bkcart.objects.filter(uid=userid)
    context={}
    context['data']=orders
    b=0
    m=0
    booking=999
    for x in orders:
        m=m+x.mid.package*x.qty
        b=b+x.bid.rent*x.qty
    np=len(orders)
    
    context['items']=np
    context['total']=booking
    return render(request, 'bkplaceorder.html',context)

def bkfinalplaceorder(request):
    userid=request.user.id
    c=bkcart.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)

    for x in c:
        o=order.objects.create(order_id=oid,
                               qty=x.qty,mid=x.mid,uid=x.uid,bid=x.bid,)
        o.save()
        x.delete()
    orders=order.objects.filter(uid=userid)
    context={}
    context['data']=orders
    b=0
    m=0
    booking=999
    for x in orders:
        m=m+x.mid.package*x.qty
        b=b+x.bid.rent*x.qty
    np=len(orders)
    
    context['items']=np
    context['total']=m+b
    return render(request, 'cart.html',context)


def bremove(request,uid):
    c=order.objects.filter(id=uid)
    c=c.delete()
    return redirect('/cart')

def mremove(request,uid):
    c=order.objects.filter(id=uid)
    c=c.delete()
    return redirect('/cart')

def cmremove(request,uid):
    c=order.objects.filter(id=uid)
    c=c.delete()
    
    return redirect('/banqpreview')
    #return render(request,'confirmmenu.html')

def updateqty(request,qv,mid):
    c=order.objects.filter(id=mid)
    if qv=='1':
        t=c[0].qty+1
        c.update(qty=t)
    else:
        if c[0].qty>1:
            t=c[0].qty-1
            c.update(qty=t)
    return redirect('/cart')

def makepayment(request):  
    orders=morder.objects.filter(uid=request.user.id) 
    b=0
    m=0
    np=len(orders)
    for x in orders:
        m=m+x.mid.package*x.qty
        b=b+x.bid.rent*x.qty
        oid=x.order_id

    client = razorpay.Client(auth=("rzp_test_olwOP61TwNTH38", "9ENJ2Q5RDDN7GlkAuDDH2G4i"))

    data = { "amount": b*100+m*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    context={}
    context['data']=payment
    uemail=request.user.username
    context['uemail']=uemail
    return render(request,'pay.html',context)

def bkmakepayment(request):  
    orders=bkcart.objects.filter(uid=request.user.id) 
    b=0
    m=0
    np=len(orders)
    for x in orders:
        m=m+x.mid.package*x.qty
        b=b+x.bid.rent*x.qty
        oid=x.order_id

    client = razorpay.Client(auth=("rzp_test_olwOP61TwNTH38", "9ENJ2Q5RDDN7GlkAuDDH2G4i"))

    data = { "amount": 999*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    context={}
    context['data']=payment
    uemail=request.user.username
    context['uemail']=uemail
    return render(request,'pay.html',context)

def menuview(request):

    m=menu.objects.filter(is_active=True)
    context={}
    context['Menu']=m

    indveg=dishes.objects.filter(mid=1)
    context['indveg']=indveg

    indnonveg=dishes.objects.filter(mid=2)
    context['indnonveg']=indnonveg

    chinese=dishes.objects.filter(mid=3)
    context['chinese']=chinese

    continental=dishes.objects.filter(mid=4 )
    context['continental']=continental

    MaharastrianAgriKoli=dishes.objects.filter(mid=5 )
    context['MaharastrianAgriKoli']=MaharastrianAgriKoli

    Malvani=dishes.objects.filter(mid=6 )
    context['Malvani']=Malvani

    SouthIndian=dishes.objects.filter(mid=7 )
    context['SouthIndian']=SouthIndian

    Rajastani=dishes.objects.filter(mid=8 )
    context['Rajastani']=Rajastani


    return render(request,'menu.html',context)

def offers(request):
    return render(request,'offers.html')

def mportal(request):
    uid=request.user.id
    u=User.objects.get(id=uid)
    return render(request,'MPortal.html')

def custbooking(request):
    o=morder.objects.filter(uid=request.user.id)
    context={}
    bk=bkcart.objects.filter(uid=request.user.id)
    context={}
    context['bkorder']=bk
    
    context['morder']=o
    print(bk)
    print(o)

    
    return render(request,'custbooking.html',context)

def confirmm(request,mid):
    uid=request.user.id
    m=order.objects.filter(id=mid)
    context={}
    context['Menu']=m
    

    return render(request,'confirmmenu.html',context)


