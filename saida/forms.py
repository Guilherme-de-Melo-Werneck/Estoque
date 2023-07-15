from django.forms import ModelForm
from .models import Saidas
from django.forms import TextInput, Select, Textarea, NumberInput

class NotaSaidasForm(ModelForm):
    class Meta:
        model = Saidas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'produto': Select(attrs={'class':'select'}),
            'quantidade': NumberInput(attrs={'class':'numberinput'}),
            'preco': NumberInput(attrs={'class':'input'}),
        }