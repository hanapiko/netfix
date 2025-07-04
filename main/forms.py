from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from main.models import AppUser

ACTIVITY_CHOICES_FORM = [
    ('ALL_IN_ONE', 'All in One'),
    ('AIR_CONDITIONER', 'Air Conditioner'),
    ('CARPENTRY', 'Carpentry'),
    ('ELECTRICITY', 'Electricity'),
    ('GARDENING', 'Gardening'),
    ('HOME_MACHINES', 'Home Machines'),
    ('HOUSEKEEPING', 'Housekeeping'),
    ('INTERIOR_DESIGN', 'Interior Design'),
    ('LOCKS', 'Locks'),
    ('PAINTING', 'Painting'),
    ('PLUMBING', 'Plumbing'),
    ('WATER_HEATERS', 'Water Heaters'),
]
"""have no CUSTOMER , ALL_IN_ONE used default"""


class CompanyCreationForm(UserCreationForm):
    # add new unique fields to built-in UserCreationForm
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    field_of_work = forms.ChoiceField(
        required=True, choices=ACTIVITY_CHOICES_FORM,
         initial='ALL_IN_ONE')

    class Meta:
        # this model will be used to create the form based on fields of model
        model = AppUser
        # these fields will be shown in the form.
        fields = ('username', 'email', 'field_of_work',
                  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set autofocus on username field when page is loaded
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Enter your username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if AppUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if AppUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use")
        return email

    def save(self, commit=True):
        company = super().save(commit=False)
        company.email = self.cleaned_data['email']
        company.field_of_work = self.cleaned_data['field_of_work']
        # fill the field which is required but not shown in the form
        company.date_of_birth = timezone.now()
        if commit:
            # save the data in the form to the database happens here
            company.save()
        return company


class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    date_of_birth = forms.DateField(
        required=True, widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter date of birth'}))

    class Meta:
        model = AppUser
        fields = ('username', 'email', 'date_of_birth',
                  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Enter your username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if AppUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if AppUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use")
        return email

    def save(self, commit=True):
        customer = super().save(commit=False)
        customer.email = self.cleaned_data['email']
        customer.date_of_birth = self.cleaned_data['date_of_birth']
        if commit:
            customer.save()
        return customer


# make userloginform using email+ password instead of username + password
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your mail'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = AppUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus'})
