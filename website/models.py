from django.db import models

class Prato(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    tempo = models.IntegerField()
    imagem = models.ImageField(upload_to="pratos/", blank=True)

    def __str__(self):
        return self.nome