# Generated by Django 5.0.3 on 2024-04-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('ID_ARPESSOA', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAME_ARPESSOA', models.CharField(max_length=100)),
                ('CPF_ARPESSOA', models.IntegerField(verbose_name=12)),
                ('CITY_ARPESSOA', models.CharField(max_length=100)),
                ('DTCRIACAO_ARPESSOA', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
