from django import forms
from .models import Laptop


class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        labels = {
            'company': 'Enter Company Name',
            'model_name': 'Enter Model Name',
            'ram': 'Enter RAM',
            'rom': 'Enter ROM',
            'processor': 'Enter Processor',
            'price': 'Enter Price',
            'weight': 'Enter Weight'
        }

        widgets = {
            'ram': forms.TextInput(attrs={
                'placeholder': 'RAM should be in GB'
            }),
            'rom':forms.TextInput(attrs={'placeholder': 'ROM should be in GB'})
        }

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram <= 0:
            raise forms.ValidationError("RAM must be greater than Zero.")
        elif ram % 2 != 0:
            raise forms.ValidationError("Please enter RAM in EVEN number.")
        else:
            return ram


    def clean_rom(self):
        rom = self.cleaned_data['rom']
        if rom <= 0:
            raise forms.ValidationError("ROM must be greater than Zero.")
        else:
            return rom


