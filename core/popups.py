from django import forms
from core.models import PedidoItem, Pedido
from popup.views import PopupCRUDViewSet

class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = '__all__'
        exclude = ('user',)

class PedidoItemPopupCRUDViewSet(PopupCRUDViewSet):
    model = PedidoItem
    form_class = PedidoItemForm
