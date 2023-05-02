# Generated by Django 4.2 on 2023-05-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarySearch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_cover',
            new_name='capa_livro',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_title',
            new_name='nome_livro',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='number_copies',
            new_name='numero_copias',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='about',
            new_name='sobre',
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[(1, 'Disponivel'), (2, 'Alugado'), (3, 'Reservado')], default='Disponivel', max_length=20),
        ),
    ]