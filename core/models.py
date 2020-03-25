from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    PRODUTOS = (
        ('Pizza Grande', 'Pizza Grande'),
        ('Pizza Pequena', 'Pizza Pequena'),
        ('Esfiha', 'Esfiha'),
        ('Lanches', 'Lanches'),
        ('Sobremesa', 'Sobremesa'),
        ('Bebida', 'Bebida'),
    )

    tipo_produto = models.CharField(verbose_name='Tipo do Produto', max_length=255, choices=PRODUTOS)
    nome = models.CharField(verbose_name='Produto', max_length=255)
    preco = models.DecimalField(verbose_name='Valor do Produto', max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nome} - {self.tipo_produto}'

class PizzaGrande(models.Model):
    class Meta:
        verbose_name = 'Pizzas do Pedido'
        verbose_name_plural = 'Pizzas do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'({self.quantidade}) - {self.item} - {self.quantidade * self.item.preco}'

    def get_valor_item(self):
        return self.quantidade * self.item.preco

class PizzaBroto(models.Model):
    class Meta:
        verbose_name = 'Pizzas do Pedido'
        verbose_name_plural = 'Pizzas do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'({self.quantidade}) - {self.item} - {self.quantidade * self.item.preco}'

    def get_valor_item(self):
        return self.quantidade * self.item.preco
        
class Esfiha(models.Model):
    class Meta:
        verbose_name = 'Esfihas do Pedido'
        verbose_name_plural = 'Esfihas do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'({self.quantidade}) - {self.item} - {self.quantidade * self.item.preco}'

    def get_valor_item(self):
        return self.quantidade * self.item.preco

class Lanche(models.Model):
    class Meta:
        verbose_name = 'Lanches do Pedido'
        verbose_name_plural = 'Lanches do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'({self.quantidade}) - {self.item} - {self.quantidade * self.item.preco}'

    def get_valor_item(self):
        return self.quantidade * self.item.preco

class Sobremesa(models.Model):
    class Meta:
        verbose_name = 'Sobremesas do Pedido'
        verbose_name_plural = 'Sobremesas do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'({self.quantidade}) - {self.item} - {self.quantidade * self.item.preco}'

    def get_valor_item(self):
        return self.quantidade * self.item.preco

class Bebida(models.Model):
    class Meta:
        verbose_name = 'Sobremesas do Pedido'
        verbose_name_plural = 'Sobremesas do Pedido'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'({self.quantidade}) - {self.item} - {self.quantidade * self.item.preco}'

    def get_valor_item(self):
        return self.quantidade * self.item.preco

class Pedido(models.Model):
    class Meta:
        verbose_name = 'Pedido - Delivery'
        verbose_name_plural = 'Pedidos - Delivery'

    STATUS = (
        ('Em preparo', 'Em preparo'),
        ('Em entrega', 'Em entrega'),
        ('Concluído', 'Concluído'),
    )

    PAGAMENTOS = (
        ('Cartão', 'Cartão'),
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
    pizzas_grande = models.ManyToManyField(PizzaGrande, blank=True)
    pizzas_broto = models.ManyToManyField(PizzaBroto, blank=True)
    esfihas = models.ManyToManyField(Esfiha, blank=True)
    lanches = models.ManyToManyField(Lanche, blank=True)
    sobremesas = models.ManyToManyField(Sobremesa, blank=True)
    bebidas = models.ManyToManyField(Bebida, blank=True)
    taxa_entrega = models.DecimalField(verbose_name='Taxa de Entrega', max_digits=3, decimal_places=2, default=3)
    taxa_adicional = models.DecimalField(verbose_name='Taxas Adicionais', max_digits=3, decimal_places=2, default=0)
    desconto = models.DecimalField(verbose_name='Descontos', max_digits=3, decimal_places=2, default=0)
    pagamento = models.CharField(verbose_name='Forma de Pagamento', max_length=255, choices=PAGAMENTOS)
    pagamento_conclusao = models.CharField(verbose_name='Conclusão do Pagamento', max_length=255, choices=CONCLUSOES_PAGAMENTO, blank=True)
    necessidade_troco = models.BooleanField(verbose_name='Necessita de Troco?', default=False)
    horario_recebimento = models.DateTimeField(verbose_name='Horário de Recebimento', auto_now_add=True)
    horario_atualizacao = models.DateTimeField(verbose_name='Horário de Atualização', auto_now=True)
    status = models.CharField(verbose_name='Status do Pedido', max_length=255, choices=STATUS, default='Em preparo')
    observacao = models.TextField(verbose_name='Observações do Pedido', blank=True)

    def __str__(self):
        return f'PEDIDO: #{self.user} - {self.rua} - {self.horario_recebimento}'

    def get_valor_pedido(self):
        total = 0

        for pizza_grande in self.pizzas_grande.all():
            total += pizza_grande.get_valor_item()
        
        for pizza_broto in self.pizzas_broto.all():
            total += pizza_broto.get_valor_item()

        for esfiha in self.esfihas.all():
            total += esfiha.get_valor_item()
        
        for lanche in self.lanches.all():
            total += lanche.get_valor_item()
        
        for sobremesa in self.sobremesas.all():
            total += sobremesa.get_valor_item()
    
        for bebida in self.bebidas.all():
            total += bebida.get_valor_item()

        return total

    def get_valor_total(self):
        total = 0
        total += self.taxa_entrega
        total += self.taxa_adicional
        total -= self.desconto

        for pizza_grande in self.pizzas_grande.all():
            total += pizza_grande.get_valor_item()
        
        for pizza_broto in self.pizzas_broto.all():
            total += pizza_broto.get_valor_item()

        for esfiha in self.esfihas.all():
            total += esfiha.get_valor_item()
        
        for lanche in self.lanches.all():
            total += lanche.get_valor_item()
        
        for sobremesa in self.sobremesas.all():
            total += sobremesa.get_valor_item()
    
        for bebida in self.bebidas.all():
            total += bebida.get_valor_item()

        return total

class PedidoBalcao(models.Model):
    class Meta:
        verbose_name = 'Pedido - Balcão'
        verbose_name_plural = 'Pedidos - Balcão'

    STATUS = (
        ('Em preparo', 'Em preparo'),
        ('Pronto', 'Pronto'),
        ('Concluído', 'Concluído'),
    )

    PAGAMENTOS = (
        ('Cartão', 'Cartão'),
        ('Dinheiro', 'Dinheiro'),
    )

    CONCLUSOES_PAGAMENTO = (
        ('Dinheiro', 'Dinheiro'),
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(verbose_name="Identificação", max_length=255, blank=True)
    pizzas_grande = models.ManyToManyField(PizzaGrande, blank=True)
    pizzas_broto = models.ManyToManyField(PizzaBroto, blank=True)
    esfihas = models.ManyToManyField(Esfiha, blank=True)
    lanches = models.ManyToManyField(Lanche, blank=True)
    sobremesas = models.ManyToManyField(Sobremesa, blank=True)
    bebidas = models.ManyToManyField(Bebida, blank=True)
    desconto = models.DecimalField(verbose_name='Descontos', max_digits=3, decimal_places=2, default=0)
    pagamento_conclusao = models.CharField(verbose_name='Pagamento', max_length=255, choices=CONCLUSOES_PAGAMENTO, blank=True)
    horario_recebimento = models.DateTimeField(verbose_name='Horário de Recebimento', auto_now_add=True)
    horario_atualizacao = models.DateTimeField(verbose_name='Horário de Atualização', auto_now=True)
    status = models.CharField(verbose_name='Status do Pedido', max_length=255, choices=STATUS, default='Em preparo')
    observacao = models.TextField(verbose_name='Observações do Pedido', blank=True)

    def __str__(self):
        return f'PEDIDO: #{self.user} {self.nome} - {self.horario_recebimento}'

    def get_valor_pedido(self):
        total = 0

        for pizza_grande in self.pizzas_grande.all():
            total += pizza_grande.get_valor_item()
        
        for pizza_broto in self.pizzas_broto.all():
            total += pizza_broto.get_valor_item()

        for esfiha in self.esfihas.all():
            total += esfiha.get_valor_item()
        
        for lanche in self.lanches.all():
            total += lanche.get_valor_item()
        
        for sobremesa in self.sobremesas.all():
            total += sobremesa.get_valor_item()
    
        for bebida in self.bebidas.all():
            total += bebida.get_valor_item()

        return total

    def get_valor_total(self):
        total = 0
        total += self.taxa_entrega
        total += self.taxa_adicional
        total -= self.desconto

        for pizza_grande in self.pizzas_grande.all():
            total += pizza_grande.get_valor_item()
        
        for pizza_broto in self.pizzas_broto.all():
            total += pizza_broto.get_valor_item()

        for esfiha in self.esfihas.all():
            total += esfiha.get_valor_item()
        
        for lanche in self.lanches.all():
            total += lanche.get_valor_item()
        
        for sobremesa in self.sobremesas.all():
            total += sobremesa.get_valor_item()
    
        for bebida in self.bebidas.all():
            total += bebida.get_valor_item()

        return total
