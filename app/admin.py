from django.contrib import admin
from . models import *
# Register your models here.

class Appointment_Display(admin.ModelAdmin):
    list_display=['name','email','phone','branch','date','time','age','gender','address','message']
admin.site.register(Appointment,Appointment_Display)

class Contact_Display(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message','branch']
admin.site.register(Contact,Contact_Display)

class Enquiry_Display(admin.ModelAdmin):
    list_display=['name','email','phone','message','branch']
admin.site.register(Enquiry,Enquiry_Display)

class Branch_Display(admin.ModelAdmin):
    list_display=['name','email','image','address','number','status']
admin.site.register(Branch,Branch_Display)

class Branch_Time_Display(admin.ModelAdmin):
    list_display=['name','opening_hours','closing_hours','opening_week','closing_week']
admin.site.register(Branch_time,Branch_Time_Display)

class Package_Display(admin.ModelAdmin):
    list_display=['name','image','price','branch']
admin.site.register(Package,Package_Display)

class Subpackage_Display(admin.ModelAdmin):
    list_display=['name','content']
admin.site.register(Subpackage,Subpackage_Display)

class Order_Display(admin.ModelAdmin):
    list_display=['name','amount','package_name','branch_name','username','status']
admin.site.register(Order,Order_Display)

class Profile_Display(admin.ModelAdmin):
    list_display=['name','username','email','number','age','address','date','gender']
admin.site.register(Profile,Profile_Display)

class Testimonial_Display(admin.ModelAdmin):
    list_display=['name','branch','review']
admin.site.register(Testimonial,Testimonial_Display)

class Gallery_Display(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Gallery,Gallery_Display)
