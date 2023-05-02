from django.db import models

class Livro(models.Model):
    STATUS_CHOICES = (
        ('disponivel','Disponivel'),
        ('alugado','Alugado'),
        ('reservado','Reservado'),
    )
    
    nome_livro = models.CharField(max_length=250)
    autor = models.CharField(max_length=100)
    capa_livro = models.ImageField()
    sobre = models.TextField()
    isbn = models.CharField(max_length=50)
    numero_copias = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    
    def __str__(self):
        return self.nome_livro