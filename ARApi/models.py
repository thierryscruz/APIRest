from django.db import models
from django.core.validators import RegexValidator

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Pessoa(models.Model):
    ID_ARPESSOA = models.BigAutoField(primary_key=True)
    NAME_ARPESSOA = models.CharField(max_length=100)
    CPF_ARPESSOA = models.CharField(max_length=12, validators=[RegexValidator(regex='^[0-9]{1,12}$', message='O CPF deve conter apenas números e no máximo 12 dígitos')])
    DTNASC_ARPESSOA = models.DateField()
    CITY_ARPESSOA = models.CharField(max_length=100)
    DTCRIACAO_ARPESSOA = models.DateTimeField(auto_now_add=True)