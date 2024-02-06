from xml.sax.handler import DTDHandler
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
import os 

def getFileName(request,filename):
    now_time=dt.datetime.now().strftime("%Y %m %d %h:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join("uploads", new_filename)

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField( upload_to=getFileName,null=True,blank=True)
    discription=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self) :
        return self.name
    
    
    
class product(models.Model):  
    categorys=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    Vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    discription=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trinding=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    

    
    def __str__(self) :
        return self.name    
    
storeImage = models.ImageField(upload_to="images")