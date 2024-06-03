from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


from django import forms

from users.models import MyUser, RatePerFace, MarketPlace

class UserLogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "Enter Username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "Enter password",
    }))


    class Meta:
        model = MyUser
        fields = ['username', 'password']



class UserRegistrForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "Enter Username",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "Enter password",
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "Enter Name",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "Enter last name",
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "Enter email",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-control py-4",
        'placeholder' : "confirm your password",
    }))
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class MarketPlaceCreateForm(forms.ModelForm):
    marketplace_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control pt-2",
        'placeholder' : "Crystal 3D"}))
    rate_for_worker = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control pt-2",
        'placeholder' : "4"}))   
    rate_for_employer = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control pt-2",
        'placeholder' : "2"}))
    rate_for_admin = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control pt-2",
        'placeholder' : "2"}))

    class Meta:
        model = MarketPlace
        fields = ['marketplace_name', 'rate_for_worker', 'rate_for_employer', 'rate_for_admin']
    
    def save(self, employer_id, commit=True):
        marketplace = super().save(commit=False)
        rate = RatePerFace(
            rate_for_worker=self.cleaned_data['rate_for_worker'],
            rate_for_employer=self.cleaned_data['rate_for_employer'],
            rate_for_admin=self.cleaned_data['rate_for_admin'])
        rate.save()
        if commit:
            marketplace.employer_id = employer_id
            marketplace.rate_id = rate
            marketplace.save()
            
        return marketplace



class UserUpdateForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",

    }), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-control",

    }), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",

    }), required=False)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
    }), required=False)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
    }), required=False)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-control",
    }), required=False)

    mobile = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
    }), required=False)

    country = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
    }), required=False)

    city = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
    }), required=False)


    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'mobile', 'country', 'city']