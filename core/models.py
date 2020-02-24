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
        return f'{self.tipo_produto} - {self.nome} - Valor: R${self.preco}'

class PedidoItem(models.Model):
    class Meta:
        verbose_name = 'Itens do Pedido'
        verbose_name_plural = 'Itens do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Qntd ({self.quantidade}) - Produto: {self.item} (pedido: #{self.user})'

    def get_valor_item(self):
        return self.quantidade * self.item.preco