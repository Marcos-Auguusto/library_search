# Generated by Django 4.2 on 2023-05-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarySearch', '0003_rename_book_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(max_length=50),
        ),
    ]
