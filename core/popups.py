from django import forms
from core.models import *
from popup.views import PopupCRUDViewSet

class PizzaGrandeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PizzaGrandeForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(tipo_produto='Pizza Grande')

    class Meta:
        model = PizzaGrande
        fields = '__all__'
        exclude = ('user',)

class PizzaGrandePopupCRUDViewSet(PopupCRUDViewSet):
    model = PizzaGrande
    form_class = PizzaGrandeForm


class PizzaBrotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PizzaBrotoForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(tipo_produto='Pizza Broto')

    class Meta:
        model = PizzaBroto
        fields = '__all__'
        exclude = ('user',)

class PizzaBrotoPopupCRUDViewSet(PopupCRUDViewSet):
    model = PizzaBroto
    form_class = PizzaBrotoForm


class EsfihaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EsfihaForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(tipo_produto='Esfiha')

    class Meta:
        model = Esfiha
        fields = '__all__'
        exclude = ('user',)

class EsfihaPopupCRUDViewSet(PopupCRUDViewSet):
    model = Esfiha
    form_class = EsfihaForm


class LancheForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LancheForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(tipo_produto='Lanches')

    class Meta:
        model = Lanche
        fields = '__all__'
        exclude = ('user',)

class LanchePopupCRUDViewSet(PopupCRUDViewSet):
    model = Lanche
    form_class = LancheForm


class SobremesaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SobremesaForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(tipo_produto='Sobremesa')

    class Meta:
        model = Sobremesa
        fields = '__all__'
        exclude = ('user',)

class SobremesaPopupCRUDViewSet(PopupCRUDViewSet):
    model = Sobremesa
    form_class = SobremesaForm


class BebidaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BebidaForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(tipo_produto='Bebida')

    class Meta:
        model = Bebida
        fields = '__all__'
        exclude = ('user',)

class BebidaPopupCRUDViewSet(PopupCRUDViewSet):
    model = Bebida
    form_class = BebidaForm