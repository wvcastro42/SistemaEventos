from django.db.models.signals import post_save
from django.contrib.auth.models import User
from core.models import Ouvinte

def cria_ouvinte(sender, instance, created, **kwargs):
    if created:
        
        Ouvinte.objects.create(cpf=instance.cpf, email=instance.email, usuario=instance)
    
    
post_save.connect(cria_ouvinte, sender=User)




'''
Na tela do SignUP pegar todos os dados e associar ao user ouvinte
'''