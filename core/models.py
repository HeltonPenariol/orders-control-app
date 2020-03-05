from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    PRODUTOS = (
        ('Pizza Grande', 'Pizza Grande'),
        ('Pizza Grande (2 Sabores)', 'Pizza Grande (2 Sabores)'),
        ('Pizza Pequena', 'Pizza Pequena'),
        ('Pizza Pequena (2 Sabores)', 'Pizza Pequena (2 Sabores)'),
        ('Esfiha Aberta', 'Esfiha Aberta'),
        ('Esfiha Fechada', 'Esfiha Fechada'),
        ('Cheeseburguer', 'Cheeseburguer'),
        ('Porção', 'Porção'),
        ('Pastel', 'Pastel'),
        ('Beirute', 'Beirute'),
        ('Sobremesa', 'Sobremesa'),
        ('Bebida', 'Bebida'),
    )

    tipo_produto = models.CharField(verbose_name='Tipo do Produto', max_length=255, choices=PRODUTOS)
    nome = models.CharField(verbose_name='Produto', max_length=255)
    preco = models.DecimalField(verbose_name='Valor do Produto', max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.tipo_produto} - {self.nome}'

class PedidoItem(models.Model):
    class Meta:
        verbose_name = 'Itens do Pedido'
        verbose_name_plural = 'Itens do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Qntd ({self.quantidade}) - Produto: {self.item})'

    def get_valor_item(self):
        return self.quantidade * self.item.preco

class Pedido(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    STATUS = (
        ('Em preparo', 'Em preparo'),
        ('Em entrega', 'Em entrega'),
        ('Concluído', 'Concluído'),
    )

    PAGAMENTOS = (
        ('Maquininha', 'Maquininha'),
        ('Dinheiro', 'Dinheiro'),
    )

    CONCLUSOES_PAGAMENTO = (
        ('Dinheiro', 'Dinheiro'),
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rua = models.CharField(verbose_name='Endereço de Entrega', max_length=255)
    telefone = models.CharField(verbose_name='Telefone do Cliente', max_length=255, blank=True)
    itens = models.ManyToManyField(PedidoItem)
    taxa_entrega = models.DecimalField(verbose_name='Taxa de Entrega', max_digits=3, decimal_places=2, default=3)
    taxa_adicional = models.DecimalField(verbose_name='Taxas Adicionais', max_digits=3, decimal_places=2, default=0)
    desconto = models.DecimalField(verbose_name='Descontos', max_digits=3, decimal_places=2, default=0)
    pagamento = models.CharField(verbose_name='Forma de Pagamento', max_length=255, choices=PAGAMENTOS)
    pagamento_conclusao = models.CharField(verbose_name='Conclusão do Pagamento', max_length=255, choices=CONCLUSOES_PAGAMENTO, blank=True)
    necessidade_troco = models.BooleanField(verbose_name='Troco', default=False)
    horario_recebimento = models.DateTimeField(verbose_name='Horário de Recebimento', auto_now_add=True)
    horario_atualizacao = models.DateTimeField(verbose_name='Horário de Atualização', auto_now=True)
    status = models.CharField(verbose_name='Status do Pedido', max_length=255, choices=STATUS, default='Em preparo')
    observacao = models.TextField(verbose_name='Observações do Pedido', blank=True)

    def __str__(self):
        return f'PEDIDO: #{self.user} - {self.rua} - {self.horario_recebimento}'

    def get_valor_pedido(self):
        total = 0

        for item in self.itens.all():
            total += item.get_valor_item()
        
        return total

    def get_valor_total(self):
        total = 0
        total += self.taxa_entrega
        total += self.taxa_adicional
        total -= self.desconto

        for item in self.itens.all():
            total += item.get_valor_item()
        
        return total
