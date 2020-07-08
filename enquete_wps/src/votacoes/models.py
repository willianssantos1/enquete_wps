from django.db import models
from django.utils import timezone

class Questao (models.Model):
    questao_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data de Publicação')

    def __str__(self):
        return self.questao_text
    
    def foi_publicado_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Opcao (models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    opcao_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao_text
# Create your models here.
