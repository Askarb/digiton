from django import forms

from .models import RequestM


class RequestMCreateForm(forms.ModelForm):

    class Meta:
        model = RequestM
        fields = ('name', 'phone', 'info')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'class': 'number'}),
            'info': forms.TextInput(attrs={'placeholder': 'Расскажите чем вы занимаетесь', 'class': 'add-data'}),
        }