from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import ShopUser


class ShopUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'

            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'введите имя'
            elif field_name == 'password':
                field.widget.attrs['placeholder'] = 'введите пароль'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'

            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'введите имя'
            elif field_name == 'password':
                field.widget.attrs['placeholder'] = 'введите пароль'


class ShopUserProfileForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'

            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'введите имя'
            elif field_name == 'password':
                field.widget.attrs['placeholder'] = 'введите пароль'
