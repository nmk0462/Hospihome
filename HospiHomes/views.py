from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import User
from .models import User1
from .models import details
from .models import upd
from .models import appt
from .models import approvedapp
from .models import rate
# Create your views here.
def index(request):
    return render(request, "hospi/intro.html")
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        tyu=[]
        try:
            er=details.objects.all()
        except:
            er=None
        for t in er:
            if t.cat not in tyu:
                tyu.append(t.cat)
        # Check if authentication successful
        if user is not None:
            request.session['username'] = username
            login(request, user)
            return render(request,"hospi/search.html",{"tyu":tyu})
          
           
        
        else:
            return render(request, "hospi/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "hospi/login.html")

def login_view1(request):
    pp=[]
    try:
      op=User1.objects.all()
    except:
      op=None
    for t in op:
        pp.append(t.name)
    yy=request.POST.get("username1")
    request.session['username1']=yy
    yy1=request.POST.get("password1")
    if yy in pp:
        uiu=User1.objects.get(name=yy)
        if uiu.passw == yy1:
           try:
              ret=details.objects.get(usr=yy)
           except:
              ret=None
           if ret is None:
               return render(request,"hospi/detail.html")
           else:
               hy=details.objects.get(hn=ret.hn)
               return render(request,"hospi/manage.html",{"message":ret.hn,"hjl":hy})
        else:
           return render(request,"hospi/login.html",{"message1":"Check your username or password!!!"})
    else:
        return render(request,"hospi/login.html",{"message1":"User doesn't exists,please register"})
def reg(request):
    return render(request,"hospi/reg.html")
def register1(request):
   
    ty=User1()
    ty.name=request.POST.get("name2")
    huh=request.POST.get("password2")
    ty.passw=huh
    ty.hospis=request.POST.get("hname")
    hu=request.POST.get("password3")
    if huh != hu:
            return render(request, "hospi/reg.html", {
                "message": "Passwords must match."
            })
    ty.save()
    return render(request,"hospi/login.html")

    

    
def logout_view(request):
    if request.session.has_key('username'):

       del request.session['username']
    if request.session.has_key('username1'):

       del request.session['username1']
    logout(request)
    
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "hospi/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "hospi/register.html", {
                "message": "Username already taken."
            })
        request.session['username'] = username
        login(request, user)
        return render(request,"hospi/login.html")
        
        
    else:
        return render(request, "hospi/register.html")
def go(request):
    lol=details()
    lol.usr=request.session['username1']
    ko=request.POST.get("hosnam").upper()
    lol.hn=ko
    lol.addr=request.POST.get("addr")
    lol.specs=request.POST.get("spec")
    lol.docts=request.POST.get("doc")
    lol.cat=request.POST.get("cat")
    lol.conts=request.POST.get("cont")
    lol.amb=request.POST.get("amb")
    lol.beds=request.POST.get("beds")
    lol.pic=request.POST.get("pic")
    try:
        ret=details.objects.get(usr=request.session['username1'])
    except:
        ret=None
    lol.save()
    return render(request,"hospi/manage.html",{"message":ko,"hjl":ret})
def srh(request):
    ru=details()
    dd=request.POST.get("sh")
    try:
        rr=dd
        hii=details.objects.filter(cat=dd)
    except:
        hii=None
    try:
        hii1=details.objects.filter(hn=dd)
    except:
        hii1=None
    tyu=[]
    try:
        er=details.objects.all()
    except:
        er=None
    for t in er:
        if t.cat not in tyu:
           tyu.append(t.cat)
    
    return render(request,"hospi/search.html",{"tt":hii,"tt1":hii1,"tyu":tyu})
def hosp(request,nm):
    gy=details.objects.get(hn=nm)
    try:
       tut=upd.objects.get(hnm=nm)
    except:
       tut=None
    cc=details.objects.get(hn=nm)
    try:
       hy=rate.objects.filter(hos=nm)
    except:
        hy=None
    ll=0
    count=0
    if hy!=None:
        for h in hy:
            count=count+1
            ll=ll+h.raa
    if count==0:
        cc.avg=0
        cc.save()
    else:
        cc.avg=float(ll/count)
        cc.save()
    return render(request,"hospi/main.html",{"h":gy,"k":tut})
def update(request):
    io=details.objects.get(usr=request.session['username1'])
    y=upd()
    huh=io.hn
    try:
        ko=upd.objects.get(hnm=io.hn)
    except:
        ko=None
    if ko is None:
        y.hnm=io.hn
        y.vc=request.POST.get('vac')
        y.avl=request.POST.get('avail')
        y.save()
    else:
        ko.vc=request.POST.get('vac')
        ko.avl=request.POST.get('avail')
        ko.save()
    hy=details.objects.get(hn=huh)
    return render(request,"hospi/manage.html",{"hjl":hy})
def list1(request,mn):
    lol=details.objects.filter(cat=mn)
    return render(request,"hospi/list.html",{"gh":lol})
def appoint(request,re):
    return render(request,"hospi/appoint.html",{"re":re})
def apsub(request,re):
    pp=appt()
    pp.urr=request.session['username']
    pp.patname=request.POST.get("pat")
    pp.hnme=re
    pp.agge=request.POST.get("age")
    pp.probl=request.POST.get("prob")
    pp.datt=request.POST.get("dt")
    pp.save()
    gy=details.objects.get(hn=re)
    try:
       tut=upd.objects.get(hnm=re)
    except:
       tut=None
    cc=details.objects.get(hn=re)
    try:
       hy=rate.objects.filter(hos=re)
    except:
        hy=None
    ll=0
    count=0
    if hy!=None:
        for h in hy:
            count=count+1
            ll=ll+h.raa
    if count!=0:
        cc.avg=float(ll/count)
        cc.save()
    return render(request,"hospi/main.html",{"h":gy,"k":tut})
def check(request):
    kok=details.objects.get(usr=request.session['username1'])
    hj=appt.objects.filter(hnme=kok.hn)
    return render(request,"hospi/check.html",{"hj":hj})
def approved(request,num):
    pie=appt.objects.get(id=num)
    pip=approvedapp()
    pip.urr1=pie.urr
    hjk=pie.hnme
    hy=details.objects.get(hn=hjk)
    pip.hnma=pie.hnme
    pip.pate=pie.patname
    pip.dat=pie.datt
    pip.save()
    pie.delete()
    return render(request,"hospi/manage.html",{"message":hjk,"hjl":hy})
def back(request):
    fg=details.objects.get(usr=request.session['username1'])
    huh=fg.hn
    hy=details.objects.get(hn=huh)

    return render(request,"hospi/manage.html",{"message":fg.hn,"hjl":hy})

def your(request):
    kl=approvedapp.objects.filter(urr1=request.session['username'])
    return render(request,"hospi/your.html",{"rt":kl})

def edit(request,id):
    try:
        post = details.objects.get(id=id)
    except:
        return JsonResponse({"error": "Post not found."}, status=404)
    if request.method=="GET":
        return JsonResponse(post.serialize())
    elif request.method=="PUT":
        data=json.loads(request.body) 
        
        if data.get("conts")is not None:
            post.conts=data["conts"]
            post.docts=data["docts"]
            post.specs=data["specs"]
            post.save()
        else:
            return JsonResponse({"error":"INVALID"},status=404)
        post.save()
        return HttpResponse(status=204)
    else:
        return JsonResponse({"error":"Try GET"},status=404)
def rating(request,mk):
    pop=rate()
    rty=0
    try:
        ry=rate.objects.get(hos=mk,urr=request.session['username'])
    except:
        ry=None
    if ry == None:
        pop.urr=request.session['username']
        pop.hos=mk
        rty=request.POST.get("raat")
        pop.raa=rty
        pop.save()
    gy=details.objects.get(hn=mk)
   
    cc=details.objects.get(hn=mk)
    try:
       hy=rate.objects.filter(hos=mk)
       
    except:
        hy=None
    try:
        tut=upd.objects.get(hnm=mk)
    except:
        tut=None
    ll=0
    count=0
    if hy!=None:
        for h in hy:
            count=count+1
            ll=ll+h.raa
    if count!=0:   
        cc.avg=float(ll/count)
        cc.save()
    

    return render(request,"hospi/main.html",{"h":gy,"k":tut})
 
    
        










