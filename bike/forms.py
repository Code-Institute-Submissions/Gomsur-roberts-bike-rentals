from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'birth_date', 'phone_number', 'address', 'city', 'state', 'zip_code', 'profile_picture']
        labels = {
            'full_name': 'Full Name',
            'bio': 'Bio',
            'birth_date': 'Birth Date',
            'phone_number': 'Phone Number',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip Code',
            'profile_picture': 'Profile Picture',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }