from django import forms
from .models import Contact

# Create your forms here.

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		exclude = ()
		feilds = ['subject', 'name', 'email', 'message']
		
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))

	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' }))
	message = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control' }))