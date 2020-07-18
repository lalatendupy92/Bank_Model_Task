from django import forms
from .models import *
class User_Details_Fill(forms.ModelForm):
    class Meta:
        model=User_Details
        fields='__all__'
        exclude = ('user_status',)

    user_name = forms.CharField(label='Name:', help_text="*Only char's")
    user_phone = forms.IntegerField(label='Contact No:', )
    user_email = forms.EmailField(label='Email Id:')
    user_photo = forms.ImageField(label='Image:')

