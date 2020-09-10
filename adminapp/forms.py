import django.forms as forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CleanAgeMixin:
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return data


class AdminShopUserCreateForm(UserCreationForm, CleanAgeMixin):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'is_superuser', 'is_staff',
                  'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            # field.help_text = ''  # очистка стандартного справочного текста (слишком громоздкий)

            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'введите имя'
                field.help_text = '* обязательное поле'
                field.label += '*'
            elif field_name == 'password1' or field_name == 'password2':
                field.widget.attrs['placeholder'] = 'введите пароль'
                field.help_text = '* обязательное поле'
                field.label += '*'
            elif field_name == 'age':
                field.widget.attrs['placeholder'] = 'введите возраст'
                field.help_text = '* обязательное поле'
                field.label += '*'

    # def clean_avatar(self):
    #     pass
