from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus



# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField(max_length=500)

class Enquiry(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    message=models.TextField(max_length=500)

class Branch(models.Model):
    name=models.CharField(max_length=255,unique=True)
    image=models.CharField(max_length=3000)
    address=models.TextField(max_length=500)
    number=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Branch_time(models.Model):
    name=models.ForeignKey(Branch,on_delete=models.CASCADE)
    opening_hours=models.CharField(max_length=300)
    closing_hours=models.CharField(max_length=300)
    opening_week=models.CharField(max_length=300)
    closing_week=models.CharField(max_length=300,null=True)


    

class Package(models.Model):
    name=models.CharField(max_length=255,unique=True)
    image=models.CharField(max_length=3055)
    price=models.IntegerField()
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subpackage(models.Model):
    name=models.ForeignKey(Package,on_delete=models.CASCADE)
    content=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    package_name = models.ForeignKey(Package,on_delete=models.CASCADE)
    branch_name = models.ForeignKey(Branch,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)


    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


class Appointment(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    date=models.DateField(max_length=255)
    time=models.TextField(max_length=255)
    age=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    address=models.TextField(max_length=255)
    message=models.TextField(max_length=255,null=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)

   

class Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    age=models.CharField(max_length=300)
    address=models.TextField(max_length=500)
    gender=models.CharField(max_length=300)
    number=models.CharField(max_length=300)
    date=models.DateField(max_length=255)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=355)
    branch=models.ForeignKey(Branch,max_length=355,on_delete=models.CASCADE)
    review=models.TextField(max_length=500)
        
    def __str__(self):
        return self.name


class Gallery(models.Model):
    image=models.ImageField(upload_to="gallery/")




