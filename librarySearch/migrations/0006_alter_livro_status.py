# Generated by Django 4.2 on 2023-05-02 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarySearch', '0005_alter_livro_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='status',
            field=models.CharField(choices=[('disponivel', 'Disponivel'), ('alugado', 'Alugado'), ('reservado', 'Reservado')], default='disponivel', max_length=20),
        ),
    ]
