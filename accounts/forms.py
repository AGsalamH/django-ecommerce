from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login

UserModel = get_user_model()



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email','first_name', 'last_name')


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(widget=forms.widgets.PasswordInput, required=True)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user_exists = UserModel.objects.filter(email=email).exists()
        if not user_exists:
            raise forms.ValidationError('A user attached to this email does NOT exist.')

        self._authenticate()

        return cleaned_data
    

    def _authenticate(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(self.request, email=email, password=password)
        if not user:
            raise forms.ValidationError('Email or password is NOT correct!!')
        
        if not user.is_active:
            raise forms.ValidationError('This user can\'t login. (inactive)')

        self.user = user
    
    def get_user(self):
        return self.user