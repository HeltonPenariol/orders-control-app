from django import forms
from core.models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ('user',)