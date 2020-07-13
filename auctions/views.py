from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Listings
from .models import User
from .models import Bids
from .models import Comments
from .models import Watchlist
from .models import Winners1
import time
all6=[]
ll=[]

def start(request):
    return render(request,"auctions/start.html")
def index(request):
    try:
       all =Listings.objects.all()
       if all:
           return render(request, "auctions/index.html",{"tt":all})
       else:
           return render(request, "auctions/index.html",{"tt":all,"re":"No active listings 🙁"})

    except:
        return render(request, "auctions/index.html",{"tt":all,"re":"No active listings 🙁"})
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            request.session['username'] = username
            login(request, user)
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    if request.session.has_key('username'):

       del request.session['username']
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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        request.session['username'] = username
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
def create(request):
    return render(request,"auctions/create.html")
def created(request):
  if request.method =="POST":
   
    post=Listings()
    post.title1= request.POST.get('title1')
    post.desc= request.POST.get('desc')
    post.bid= request.POST.get('bid')
    post.cat= request.POST.get('cat') 
    post.lnk= request.POST.get('lnk')
    post.usrr=request.session['username']
    ts = time.localtime()
  
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    post.crt=timestamp
    post.save()
    all =Listings.objects.all()
 
    return render(request, "auctions/index.html",{"tt":all})
  else:
    return HttpResponse("Not allowed go back and login again")
   
def bid(request,mk1):
  
  if request.session.has_key('username'):
      try:
        all1l =Listings.objects.get(id=mk1)
        pp=Watchlist.objects.get(titlee=mk1,usrs1=request.session['username'])
      except Listings.DoesNotExist:
        return HttpResponse("errorrrrr")
      except Watchlist.DoesNotExist:
        pp=None
      cm=Comments.objects.filter(titl=mk1)
      if all1l.usrr==request.session['username']:
        if pp:
           return render(request,"auctions/bid.html",{"mk":all1l ,"cls":True,"cm":cm,"u":False})
        else:
           return render(request,"auctions/bid.html",{"mk":all1l ,"cls":True,"cm":cm,"u":True})
      else:
        if pp:
           return render(request,"auctions/bid.html",{"mk":all1l ,"cls":False,"cm":cm,"u":False})
        else:
           return render(request,"auctions/bid.html",{"mk":all1l ,"cls":False,"cm":cm,"u":True})
       

  else:
      return render(request,"auctions/login.html")
def bid1(request,mk2):
    if request.session.has_key('username'):
      
      post=Bids()
      post.title2=mk2
      all2 =Listings.objects.get(id=mk2)
      com=int(request.POST.get('bids1'))
      if com>int(all2.bid):
        post.bids= request.POST.get('bids1')
        post.unm = request.session['username']
        all2.bid=com
        
        all2.save()
        post.save()
        return HttpResponseRedirect(reverse('bid',args=(mk2,)))
      else:
        return HttpResponseRedirect(reverse('bid',args=(mk2,)))
def comm(request,mm):
    post1=Comments()
    post1.cmnt=request.POST.get('cmnt')
    post1.usrs=request.session['username']
    post1.titl=mm
    post1.save()
    return HttpResponseRedirect(reverse('bid',args=(mm,)))

    
def win(request,mk3):
    all3 =Listings.objects.get(id=mk3)
    qw=Comments.objects.filter(titl=mk3)
    iuy=Bids.objects.filter(title2=mk3)
    try:
        ss=Bids.objects.get(title2=mk3 , bids=all3.bid)
        win=ss.unm
    except:
        win="No bids"

    post=Winners1()
    post.userwin=win
    post.tll=mk3
    post.desc1=all3.desc
    post.bidd1=all3.bid
    post.cat1=all3.cat
    post.lnk1=all3.lnk
    post.save()
    all3.delete()
    qw.delete()
    iuy.delete()
    
    return render(request,"auctions/win.html",{"win":win,"tt":all3})
def watchlist(request,mk4):
    post=Watchlist()
    post.titlee=mk4
    post.usrs1=request.session['username']
    post.save()
    return HttpResponseRedirect(reverse('bid',args=(mk4,)))
def remwatchlist(request,mkk):
    fk=Watchlist.objects.get(titlee=mkk,usrs1=request.session['username'])
    fk.delete()
    return HttpResponseRedirect(reverse('bid',args=(mkk,)))
def my(request):
    all6=[]
    all5=Watchlist.objects.filter(usrs1=request.session['username'])
    if not all5:
       return render(request,"auctions/watchlist.html",{"wwttf":"No watchlists :("}) 
    else:
        for r in all5:
          if not Listings.objects.filter(id=r.titlee) :
              erf=False
          else:
              erf=True
              all6.append(Listings.objects.filter(id=r.titlee))
        
        if not erf:
            return render(request,"auctions/watchlist.html",{"wwttf":"Bid has been closed by the owner,if you have won the bid you can see details at 'Bids won by me:)' or else the bid has been won by the other user." })
        else:
            return render(request,"auctions/watchlist.html",{"wwtt":all6})
def cate(request):
    ll=[]
    categ=Listings.objects.all()
    for y in categ:
        if y.cat  not in ll:

          ll.append(y.cat)
        
        
    return render(request,"auctions/categories.html",{"ii":ll})
def lists(request,jj):
    lu=Listings.objects.filter(cat=jj)
    return render(request,"auctions/catelist.html",{"uu":lu})
def winnerlist(request):
    io=[]
    op=Winners1.objects.filter(userwin=request.session['username'])
    if not op:
        return render(request,"auctions/winners.html",{"qqq":"Not won anything yet :("})

    else:

        return render(request,"auctions/winners.html",{"qq":op})
