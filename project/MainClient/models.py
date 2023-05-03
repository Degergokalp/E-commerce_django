from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
import random
import string
from django.urls import reverse

#utilities for instances

def Id_generator():
    Id=random.randint(0,999999999)
    converted_Id=str(Id)
    if CustomerProfile.objects.filter(customerId=converted_Id).exists()==False:
          
           return converted_Id
    else:
        return Id_generator()

def LoggedUser(request):
	currentUserid=request.user.id
	return currentUserid

def LoggedUserName(request):
	currentUserName=User.username
	return currentUserName


def slug_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    slug=''.join(random.choice(chars) for _ in range(size))
    if Items.objects.filter(slug=slug).exists()==False:
          return slug
    else:
        return slug_generator()

class CustomerProfile(models.Model):
    user=models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    customerId=models.CharField(max_length=10 ,blank=True)   #Uniq Id

class Wallet(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,default=' ')
    balance=models.IntegerField(blank=True,default=0)
    slug=models.SlugField(max_length=100,blank=True)

    def __str__(self):
        return self.name
    def __int__(self):
        return self.user_id

class Items(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    slug=models.SlugField(max_length=100,blank=True)

class CartItems(models.Model):
    user=models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE,null=True, default=None)
    quantity = models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)

    def total_price(self):
        return self.quantity * self.item.price
    

class Orderss(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItems)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    
    
class Address(models.Model):
    user=models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=5)
    apartment_no=models.CharField(max_length=25)
    daire=models.CharField(max_length=5)
    slug=models.SlugField(max_length=100, blank=True)



@receiver(post_save,sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
       CustomerProfile.objects.create(user=instance)
       Wallet.objects.create(user=instance)
       Address.objects.create(user=instance)
    
def pre_save_ID(sender,instance, *args, **kwargs ):
    if not instance.customerId:
        instance.customerId=Id_generator()
pre_save.connect(pre_save_ID,sender=CustomerProfile)

def pre_save_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=slug_generator()
pre_save.connect(pre_save_slug,sender=Items)
pre_save.connect(pre_save_slug,sender=Wallet)
pre_save.connect(pre_save_slug,sender=Address)



def pre_save_LoggedUser(sender,instance, *args, **kwargs ):
    if not instance.user:
        instance.user=LoggedUser
pre_save.connect(pre_save_LoggedUser,sender=CustomerProfile)
pre_save.connect(pre_save_LoggedUser,sender=Wallet)
pre_save.connect(pre_save_LoggedUser,sender=Address)





       


        
       






