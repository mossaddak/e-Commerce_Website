from .models import Profile_picture
from django import forms
from django.contrib.auth.models import User

class cnge_profile(forms.ModelForm):
    Profile_picture = forms.ImageField(widget=forms.FileInput())
    class Meta:
        model = Profile_picture
        fields = ('Profile_picture',)

class change_profile_info(forms.ModelForm):
    first_name = forms.CharField(widget=forms.FileInput(attrs={'class':"form-control"}))
    last_name = forms.CharField(widget=forms.FileInput(attrs={'class':"form-control"}))
    email = forms.EmailField(widget=forms.FileInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields = ('first_name','last_name','email',)

    




