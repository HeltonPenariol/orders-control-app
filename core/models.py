from django.db import models
from django.contrib.auth.models import User

from .choices import *

import decimal

class Pedido(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    numero_identificacao = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_pedido = models.CharField(verbose_name='Categoria do Pedido', max_length=255, choices=TIPO_PEDIDO)
    identificacao = models.CharField(verbose_name='Identificação do Pedido', max_length=255, blank=True)
    telefone = models.CharField(verbose_name='Telefone do Cliente', max_length=255, blank=True)
    observacao = models.TextField(verbose_name='Observações do Pedido', blank=True)
    taxa = models.DecimalField(verbose_name='Taxa de Entrega', max_digits=3, decimal_places=2, default=0)
    adicional = models.DecimalField(verbose_name='Taxas Adicionais', max_digits=3, decimal_places=2, default=0)
    desconto = models.DecimalField(verbose_name='Descontos', max_digits=3, decimal_places=2, default=0)
    total = models.DecimalField(verbose_name='Total', max_digits=10, decimal_places=2, default=0.00)
    pagamento_solicitado = models.CharField(verbose_name='Pagamento Solicitado', max_length=255, choices=PAGAMENTOS, blank=True)
    dinheiro_recebido = models.DecimalField(verbose_name='Recebimento de Dinheiro', max_digits=5, decimal_places=2, default=0, blank=True)
    debito_recebido = models.DecimalField(verbose_name='Recebimento de Débito', max_digits=5, decimal_places=2, default=0, blank=True)
    credito_recebido = models.DecimalField(verbose_name='Recebimento de Crédito', max_digits=5, decimal_places=2, default=0, blank=True)
    status = models.CharField(verbose_name='Status do Pedido', max_length=255, choices=STATUS, default='Em preparo')
    
    horario_recebimento = models.DateTimeField(verbose_name='Horário de Recebimento', auto_now_add=True)
    horario_atualizacao = models.DateTimeField(verbose_name='Horário de Atualização', auto_now=True)

    def checar_recebidos(self):
        if self.dinheiro_recebido + self.debito_recebido + self.credito_recebido >= self.total:
            return True
        else:
            return False
    
    def checar_dinheiro(self):
        total = self.dinheiro_recebido
        return total

    def checar_debito(self):
        total = self.debito_recebido
        return total

    def checar_credito(self):
        total = self.credito_recebido
        return total

    def __str__(self):
        return f'{self.horario_recebimento} PEDIDO: #{self.numero_identificacao} {self.identificacao}'

class RecheioPizza(models.Model):
    class Meta:
        verbose_name = '91. Recheio de Pizza'
        verbose_name_plural = '91. Recheios de Pizza'

    nome = models.CharField(verbose_name='Recheio', max_length=255, unique=True)
    preco = models.DecimalField(verbose_name='Preço do Recheio', max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.nome}'

class Pizza(models.Model):
    class Meta:
        verbose_name = '1. Pizza'
        verbose_name_plural = '1. Pizzas'

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True, related_name='pizzas')
    solicitado = models.BooleanField(default=False)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='pizzas_add_by')
    tamanho_pizza = models.CharField(verbose_name='Tamanho da Pizza', max_length=255, choices=TAMANHOS_PIZZA, default='Grande')
    borda_pizza = models.CharField(verbose_name='Borda da Pizza', max_length=255, choices=BORDAS_PIZZA, default='Sem Borda')
    recheios = models.ManyToManyField(RecheioPizza)
    quantidade_pizza = models.PositiveIntegerField(verbose_name='Quantidade' ,default=1)

    def calcular_preco(self):
        total = 0
        lista_precos = []
    
        for recheio in self.recheios.all():
            lista_precos.append(recheio.preco)

        maior_preco = max(lista_precos)
        total = maior_preco * self.quantidade_pizza

        if self.tamanho_pizza == 'Broto':
            total = total * decimal.Decimal('.75')
            total = round(total, 2)

        if self.borda_pizza == 'Borda de Catupiry' or self.borda_pizza == 'Borda de Cheddar':
            total += 5 * self.quantidade_pizza

        return total
    
    def __str__(self):
        preco = self.calcular_preco()

        if self.recheios.all().count() == 2:
            recheios = '1/2 '
            recheios += " e 1/2 ".join(str(recheio) for recheio in self.recheios.all())
            return f'{self.quantidade_pizza} Pizza(s): {self.tamanho_pizza.upper()} - {self.borda_pizza} - {recheios}, R${preco}'

        if self.recheios.all().count() == 3:
            recheios = '1/3 '
            recheios += " e 1/3 ".join(str(recheio) for recheio in self.recheios.all())
            return f'{self.quantidade_pizza} Pizza(s): {self.tamanho_pizza.upper()} - {self.borda_pizza} - {recheios}, R${preco}'

        recheios = ", ".join(str(recheio) for recheio in self.recheios.all())
        return f'{self.quantidade_pizza} Pizza(s): {self.tamanho_pizza.upper()} - {self.borda_pizza} - {recheios}, R${preco}'


class RecheioEsfiha(models.Model):
    class Meta:
        verbose_name = '92. Recheio de Esfiha'
        verbose_name_plural = '92. Recheios de Esfiha'

    recheios = models.CharField(verbose_name='Recheio da Esfiha', max_length=255)
    preco = models.DecimalField(verbose_name='Preço da Esfiha', max_digits=3, decimal_places=2)

    def __str__(self):
        return f'{self.recheios}'

class Esfiha(models.Model):
    class Meta:
        verbose_name = '2. Esfiha'
        verbose_name_plural = '2. Esfihas'

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True, related_name='esfihas')
    solicitado = models.BooleanField(default=False)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='esfihas_add_by')
    tipo = models.CharField(verbose_name='Tipo de Esfiha', max_length=255, choices=TIPO_ESFIHA, default='Aberta')
    recheio = models.ForeignKey(RecheioEsfiha, on_delete=models.CASCADE)
    quantidade_esfiha = models.PositiveIntegerField(verbose_name='Quantidade', default=1)

    def calcular_preco(self):
        total = self.recheio.preco * self.quantidade_esfiha
        return total
    
    def __str__(self):
        return f'{self.quantidade_esfiha} Esfihas(s) de {self.recheio} {self.tipo}, R${self.calcular_preco()}'

class RecheioLanche(models.Model):
    class Meta:
        verbose_name = '93. Recheio de Cheeseburguer'
        verbose_name_plural = '93. Recheios de Cheeseburguer'

    nome = models.CharField(verbose_name='Recheio', max_length=255, unique=True)
    preco = models.DecimalField(verbose_name='Preço do Recheio', max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.nome}(s)'

class Lanche(models.Model):
    class Meta:
        verbose_name = '3. Lanche'
        verbose_name_plural = '3. Lanches'

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True, related_name='lanches')
    solicitado = models.BooleanField(default=False)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='lanches_add_by')    
    recheio = models.ForeignKey(RecheioLanche, on_delete=models.CASCADE)
    quantidade_lanche = models.PositiveIntegerField(verbose_name='Quantidade', default=1)

    def calcular_preco(self):
        total = self.recheio.preco * self.quantidade_lanche
        return total

    def __str__(self):
        return f'{self.quantidade_lanche} {self.recheio}, R${self.calcular_preco()}'

class RecheioPastel(models.Model):
    class Meta:
        verbose_name = '94. Recheio de Pastel'
        verbose_name_plural = '94. Recheios de Pastel'

    nome = models.CharField(verbose_name='Recheio', max_length=255, unique=True)
    preco = models.DecimalField(verbose_name='Preço do Recheio', max_digits=4, decimal_places=2, default=7)

    def __str__(self):
        return f'{self.nome}'

class Pastel(models.Model):
    class Meta:
        verbose_name = '4. Pastel'
        verbose_name_plural = '4. Pastéis'

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True, related_name='pasteis')
    solicitado = models.BooleanField(default=False)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='pasteis_add_by')    
    recheio = models.ForeignKey(RecheioPastel, on_delete=models.CASCADE)
    quantidade_pastel = models.PositiveIntegerField(verbose_name='Quantidade', default=1)

    def calcular_preco(self):
        total = self.recheio.preco * self.quantidade_pastel
        return total

    def __str__(self):
        return f'{self.quantidade_pastel} Pastel(s) {self.recheio}, R${self.calcular_preco()}'

class RecheioBeirute(models.Model):
    class Meta:
        verbose_name = '95. Recheio de Beirute'
        verbose_name_plural = '95. Recheios de Beirute'

    nome = models.CharField(verbose_name='Recheio', max_length=255, unique=True)
    tamanho = models.CharField(verbose_name='Tamanho do Beirute', max_length=255, choices=TAMANHOS_BEIRUTE)
    preco = models.DecimalField(verbose_name='Preço do Recheio', max_digits=4, decimal_places=2)

    def __str__(self):
        return f'Beirute(s) - {self.nome} - {self.tamanho.upper()}'

class Beirute(models.Model):
    class Meta:
        verbose_name = '5. Beirute'
        verbose_name_plural = '5. Beirute'

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True, related_name='beirutes')
    solicitado = models.BooleanField(default=False)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='beirutes_add_by')    
    recheio = models.ForeignKey(RecheioBeirute, on_delete=models.CASCADE)
    quantidade_beirute = models.PositiveIntegerField(verbose_name='Quantidade', default=1)

    def calcular_preco(self):
        total = self.recheio.preco * self.quantidade_beirute
        return total

    def __str__(self):
        return f'{self.quantidade_beirute} {self.recheio}, R${self.calcular_preco()}'

class RecheioBolo(models.Model):
    class Meta:
        verbose_name = '97. Recheio de Bolo'
        verbose_name_plural = '97. Recheios de Bolo'

    nome = models.CharField(verbose_name='Recheio', max_length=255, unique=True)
    preco = models.DecimalField(verbose_name='Preço do Recheio', max_digits=4, decimal_places=2, default=7)

    def __str__(self):
        return f'Bolo(s) de {self.nome}'

class Bolo(models.Model):
    class Meta:
        verbose_name = '7. Bolo'
        verbose_name_plural = '7. Bolo'

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True, related_name='bolos')
    solicitado = models.BooleanField(default=False)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='bolos_add_by')    
    recheio = models.ForeignKey(RecheioBolo, on_delete=models.CASCADE)
    quantidade_bolo = models.PositiveIntegerField(verbose_name='Quantidade', default=1)

    def calcular_preco(self):
        total = self.recheio.preco * self.quantidade_bolo
        return total

    def __str__(self):
        return f'{self.quantidade_bolo} {self.recheio}, R${self.calcular_preco()}'

class BebidaUnidade(models.Model):
    class Meta:
        verbose_name = '96. Bebida (Unitário)'
        verbose_name_plural = '96. Bebidas (Unitário)'
    
    nome = models.CharField(verbose_name='Bebida', max_length=255, unique=True)
    tipo = models.CharField(verbose_name='Tipo de Bebida', max_length=255, choices=TIPOS_BEBIDA)
    tamanho = models.CharField(verbose_name='Tamanho da Bebida', max_length=255, choices=TAMANHOS_BEBIDA)
    preco = models.DecimalField(verbose_name='Preço do da Bebida', max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.tipo}(s) - {self.nome} {self.tamanho.upper()}'

class Bebida(models.Model):
    class Meta:
        verbose_name = '6. Bebida'
        verbose_name_plural = '6. Bebida'

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True, related_name='bebidas')
    solicitado = models.BooleanField(default=False)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='bebidas_add_by')    
    bebida = models.ForeignKey(BebidaUnidade, on_delete=models.CASCADE)
    quantidade_bebida = models.PositiveIntegerField(verbose_name='Quantidade', default=1)

    def calcular_preco(self):
        total = self.bebida.preco * self.quantidade_bebida
        return total

    def __str__(self):
        return f'{self.quantidade_bebida} {self.bebida}, R${self.calcular_preco()}'

class Cliente(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    nome = models.CharField(verbose_name="Nome do Cliente", max_length=255, blank=True)
    identificacao = models.CharField(verbose_name="Endereço", max_length=255)
    telefone = models.CharField(verbose_name="Telefone", max_length=255)

    def __str__(self):
        return f'{self.identificacao} - {self.telefone} {self.nome}'