from django import forms
from core.models import Pedido, PedidoItem
from core.popups import PedidoItemPopupCRUDViewSet

class PedidoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['itens'].widget.request = request
        self.fields['itens'].widget.attrs.update({'lay-ignore': ''})
        self.fields['itens'].queryset = PedidoItem.objects.filter(user=request.user)

    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'itens': PedidoItemPopupCRUDViewSet.get_m2m_popup_field(),
            'horario_recebimento': forms.widgets.DateTimeInput(),
            'horario_atualizacao': forms.widgets.DateTimeInput(),
       }
