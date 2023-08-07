from django import forms
from apps.pages.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'name-input',
        'placeholder': 'Ad'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'name-input',
        'placeholder': 'Soyad'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'email-input',
        'placeholder': 'Email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={  
        'class': 'email-input',
        'placeholder': 'Telefon'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={  
        "class": "input-textarea",
        'placeholder': 'Mesajınız'
    }))

    class Meta:
        model = Contact
        fields = [
            'first_name', 
            'last_name', 
            'email',
            'phone', 
            'message'
        ]
