from django import forms
from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]
        labels = {
            "name": "Название товара",
            "description": "Описание товара",
            "price": "Цена",
            "category": "Категория",
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name or len(name.strip()) < 5:
            raise forms.ValidationError("Название должно быть не менее пяти символов")
        return name

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        if price is not None and price <= 0:
            raise forms.ValidationError("Цена должна быть положительной")
        return cleaned_data
