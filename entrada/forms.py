from django.forms import ModelForm
from .models import Entradas
from django.forms import TextInput, Select, Textarea, NumberInput

class EntradaForm(ModelForm):
    class Meta:
        model = Entradas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'produto': Select(attrs={'class':'select'}),
            'quantidade': NumberInput(attrs={'class':'numberinput'}),
            'preco': NumberInput(attrs={'class':'input'}),
        }