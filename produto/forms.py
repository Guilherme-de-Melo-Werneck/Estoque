from django.forms import ModelForm
from .models import Produtos
from django.forms import TextInput, Select, Textarea

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'descricao']
        widgets = {
            'produto': TextInput(attrs={'class':'input'}),
            'cor': Select(attrs={'class':'select'}),
            'descricao': Textarea(attrs={'class':'input'}),
        }