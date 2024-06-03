from django.db import models


class Receitas(models.Model):
    nome_receita = models.CharField(max_length=30)
    ingredientes_receita = models.CharField(max_length=500)
    descricao_receita = models.TextField(max_length=1000)
