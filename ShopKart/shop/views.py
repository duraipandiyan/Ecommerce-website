from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from flask import request
from shop.form import customuserform
from . models import *

from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    products=product.objects.filter(trinding=1)
    return render(request,"shop/index.html",{"products":products})

def log_out(request):
    if redirect.user.is_authenticated:
      logout(request)
      messages.success(request,"Logged out Successfully")
    return redirect("/home")
    
def login_page(request):
    if request.method=='POST':
        name=request.POST.get("username")
        pwd=request.POST.get("password")
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully..!*") 
            return redirect("/home")
        else:
            messages.error(request,"Invalid User Name..!*") 
            return redirect('/login')
    return render(request,'shop/login.html')

def register(request):
    form=customuserform()
    if request.method=="POST":
       form=customuserform(request.POST) 
       if form.is_valid():
         form.save()
         messages.success(request,"Registerrtion success you can Login Now..!*") 
       return redirect('/login') 
    return render(request,"shop/register.html",{'form':form})

def Collections(request):
    cat=category.objects.filter(status=0)
    return render(request,"shop/Collections.html",{"cat": cat})

def Collectionview(request,name):
    if category.objects.filter(name=name,status=0):
        products=product.objects.filter(categorys__name=name)
        return render(request,"shop/products/index.html",{"products": products,"categorys__name":name})
    else:
        messages.warning(request,"NO Such Catagory Found")
        return redirect("Collections") 
    
def product_details(request,cname,pname):
  if(category.objects.filter(name=cname,status=0)):
      if(product.objects.filter(name=pname,status=0)):
          products=product.objects.filter(name=pname,status=0).first()
          return render(request,"shop/products/product_details.html",{"products":products})
      else:
          messages.error(request,"NO Surch Product Found")
          return redirect("Collections")
  else:
      messages.error(request,"No Seach Catagorery Found") 
      return redirect("Collections")   
      