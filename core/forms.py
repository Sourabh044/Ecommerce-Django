from django.forms import ModelForm
from .models import address

class AddressForm(ModelForm):
    class Meta:
        model = address
        fields = ['lat','lng']
