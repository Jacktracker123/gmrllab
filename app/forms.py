from django import forms
from . models import *
from django.contrib.auth.models import User

class Appointment_form(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'


class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'


class Enquiry_form(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields='__all__'

class Branch_form(forms.ModelForm):
    class Meta:
        model=Branch
        fields='__all__'

class Branch_timing_form(forms.ModelForm):
    class Meta:
        model=Branch_time
        fields='__all__'

class Package_add(forms.ModelForm):
    class Meta:
        model=Package
        fields='__all__'


class Profile_form(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

class Subpackage_form(forms.ModelForm):
    class Meta:
        model=Subpackage
        fields='__all__'


class Testimonial_form(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields='__all__'


class Gallery_form(forms.ModelForm):
    class Meta:
        model=Gallery
        fields='__all__'