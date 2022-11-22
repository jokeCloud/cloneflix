from django.db import models
from django.utils import timezone

LISTA_CATEGORIAS = (
    ('biografico', 'Biográfico'),
    ('humor', 'Humor'),
    ('acao', 'Ação'),
    ('outros', 'Outros'),
)

# Create your models here.


class Filme(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=100, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='thumb_filmes')

    def __str__(self):
        return self.titulo
