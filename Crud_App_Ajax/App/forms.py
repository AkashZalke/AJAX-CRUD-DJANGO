from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from .models import User

class User_data(ModelForm):
    class Meta:
        model = User
        fields =  ['name' , 'email' , 'password']
        widgets = {
            'name' : forms.TextInput(attrs={ 'class' : 'form-control' , 'id' : 'nameid'  }),
            'email' : forms.TextInput(attrs={ 'class' : 'form-control' , 'id' : 'emailid'  }),
            'password' : forms.TextInput(attrs={ 'class' : 'form-control' , 'id' : 'passwordid'  }),
        }