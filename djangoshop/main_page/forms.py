from .models import Clothes
from django.forms import ModelForm, TextInput, Textarea

class ClothesCreateForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ["title","desc","price"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название товара'
            }),
            "desc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            })
        }