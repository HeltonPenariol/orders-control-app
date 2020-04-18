from django import forms
from core.models import *

class AddPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('tamanho_pizza', 'borda_pizza', 'recheios', 'quantidade_pizza')

    recheios = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=RecheioPizza.objects.all(),
    )

class AddEsfihaForm(forms.ModelForm):
    class Meta:
        model = Esfiha
        fields = ('tipo', 'recheio', 'quantidade_esfiha')

class AddLancheForm(forms.ModelForm):
    class Meta:
        model = Lanche
        fields = ('recheio', 'quantidade_lanche')

class AddPastelForm(forms.ModelForm):
    class Meta:
        model = Pastel
        fields = ('recheio', 'quantidade_pastel')

class AddBeiruteForm(forms.ModelForm):
    class Meta:
        model = Beirute
        fields = ('recheio', 'quantidade_beirute')

class AddBoloForm(forms.ModelForm):
    class Meta:
        model = Bolo
        fields = ('recheio', 'quantidade_bolo')

class AddBebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ('bebida', 'quantidade_bebida')

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('tipo_pedido', 'identificacao', 'telefone', 'observacao', 'pagamento_solicitado', 'taxa', 'adicional', 'desconto')

class RecebidosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('dinheiro_recebido', 'debito_recebido', 'credito_recebido')

class StatusForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('status',)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
