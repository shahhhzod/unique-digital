# forms.py

from django import forms
from .models import Inquiry
class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['full_name', 'phone', 'email', 'project_type', 'description']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-inquiry w-100', 'placeholder': 'Полное имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-inquiry w-100', 'placeholder': 'Телефон'}),
            'email': forms.EmailInput(attrs={'class': 'form-inquiry  w-100', 'placeholder': 'Email'}),
            'project_type': forms.Select(attrs={'class': 'form-inquiry  w-100'}, choices=[
                ('', 'Выберите тип проекта'),  # Пустой выбор как начальное значение
                ('Комплексный', 'Комплексный'),
                ('Брендинг', 'Брендинг'),
                ('Веб-проект', 'Веб-проект'),
                ('SMM', 'SMM')
            ]),
            'description': forms.Textarea(attrs={'class': 'form-inquiry-msg  w-100', 'placeholder': 'Опишите задачу'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }