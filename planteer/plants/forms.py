# plants/forms.py
from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'about', 'used_for', 'image', 'category', 'is_edible']
        category = forms.ChoiceField(
            choices=Plant.Category.choices,
            widget=forms.Select(attrs={'class': 'form-control'})
        )