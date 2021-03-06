# Generated by Django 2.1.3 on 2018-12-03 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('data_exp', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='clientes',
            name='cpf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.CPF'),
        ),
    ]
