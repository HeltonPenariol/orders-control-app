from django import forms
from core.models import *
from core.popups import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['pizzas_grande'].widget.request = request
        self.fields['pizzas_broto'].widget.request = request
        self.fields['esfihas'].widget.request = request
        self.fields['lanches'].widget.request = request
        self.fields['sobremesas'].widget.request = request
        self.fields['bebidas'].widget.request = request
        self.fields['pizzas_grande'].widget.attrs.update({'lay-ignore': ''})
        self.fields['pizzas_broto'].widget.attrs.update({'lay-ignore': ''})
        self.fields['esfihas'].widget.attrs.update({'lay-ignore': ''})
        self.fields['lanches'].widget.attrs.update({'lay-ignore': ''})
        self.fields['sobremesas'].widget.attrs.update({'lay-ignore': ''})
        self.fields['bebidas'].widget.attrs.update({'lay-ignore': ''})
        self.fields['pizzas_grande'].queryset = PizzaGrande.objects.filter(user=request.user)
        self.fields['pizzas_broto'].queryset = PizzaBroto.objects.filter(user=request.user)
        self.fields['esfihas'].queryset = Esfiha.objects.filter(user=request.user)
        self.fields['lanches'].queryset = Lanche.objects.filter(user=request.user)
        self.fields['sobremesas'].queryset = Sobremesa.objects.filter(user=request.user)
        self.fields['bebidas'].queryset = Bebida.objects.filter(user=request.user)

    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ('user', 'status', 'pagamento_conclusao',)
        widgets = {
            'pizzas_grande': PizzaGrandePopupCRUDViewSet.get_m2m_popup_field(),
            'pizzas_broto': PizzaBrotoPopupCRUDViewSet.get_m2m_popup_field(),
            'esfihas': EsfihaPopupCRUDViewSet.get_m2m_popup_field(),
            'lanches': LanchePopupCRUDViewSet.get_m2m_popup_field(),
            'sobremesas': SobremesaPopupCRUDViewSet.get_m2m_popup_field(),
            'bebidas': BebidaPopupCRUDViewSet.get_m2m_popup_field(),
            'taxa_entrega': forms.NumberInput(attrs={'id': 'taxa_entrega'}),
            'taxa_adicional': forms.NumberInput(attrs={'id': 'taxa_adicional'}),
            'desconto': forms.NumberInput(attrs={'id': 'desconto'}),
       }

class StatusPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['status', 'pagamento_conclusao',]

class PedidoBalcaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(PedidoBalcaoForm, self).__init__(*args, **kwargs)
        self.fields['pizzas_grande'].widget.request = request
        self.fields['pizzas_broto'].widget.request = request
        self.fields['esfihas'].widget.request = request
        self.fields['lanches'].widget.request = request
        self.fields['sobremesas'].widget.request = request
        self.fields['bebidas'].widget.request = request
        self.fields['pizzas_grande'].widget.attrs.update({'lay-ignore': ''})
        self.fields['pizzas_broto'].widget.attrs.update({'lay-ignore': ''})
        self.fields['esfihas'].widget.attrs.update({'lay-ignore': ''})
        self.fields['lanches'].widget.attrs.update({'lay-ignore': ''})
        self.fields['sobremesas'].widget.attrs.update({'lay-ignore': ''})
        self.fields['bebidas'].widget.attrs.update({'lay-ignore': ''})
        self.fields['pizzas_grande'].queryset = PizzaGrande.objects.filter(user=request.user)
        self.fields['pizzas_broto'].queryset = PizzaBroto.objects.filter(user=request.user)
        self.fields['esfihas'].queryset = Esfiha.objects.filter(user=request.user)
        self.fields['lanches'].queryset = Lanche.objects.filter(user=request.user)
        self.fields['sobremesas'].queryset = Sobremesa.objects.filter(user=request.user)
        self.fields['bebidas'].queryset = Bebida.objects.filter(user=request.user)

    class Meta:
        model = PedidoBalcao
        fields = '__all__'
        exclude = ('user', 'status',)
        widgets = {
            'pizzas_grande': PizzaGrandePopupCRUDViewSet.get_m2m_popup_field(),
            'pizzas_broto': PizzaBrotoPopupCRUDViewSet.get_m2m_popup_field(),
            'esfihas': EsfihaPopupCRUDViewSet.get_m2m_popup_field(),
            'lanches': LanchePopupCRUDViewSet.get_m2m_popup_field(),
            'sobremesas': SobremesaPopupCRUDViewSet.get_m2m_popup_field(),
            'bebidas': BebidaPopupCRUDViewSet.get_m2m_popup_field(),
            'desconto': forms.NumberInput(attrs={'id': 'desconto', 'step': 0.5}),
       }

class StatusPedidoBalcaoForm(forms.ModelForm):
    class Meta:
        model = PedidoBalcao
        fields = ['status', 'pagamento_conclusao',]