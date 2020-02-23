from django.db import models

class Item(models.Model):
    class Meta:
        verbose_name = 'Iten'

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
        return f'{self.tipo_produto} - {self.nome} - Valor: {self.preco}'
    
