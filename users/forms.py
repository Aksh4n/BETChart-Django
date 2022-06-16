from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from .models import UserBankAccount

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' }))
    def clean_email(self):
        
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']
        
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
    def clean_username(self):
        
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("the given username is already registered")
        return self.cleaned_data['username']


    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2' )

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'


class WalletAddressForm(forms.ModelForm):
	class Meta:
		model = UserBankAccount
        
		exclude = ('user' , 'balance' , 'initial_deposit_date' , 'account_no',)
		feilds = ['walletaddress']


   
      






