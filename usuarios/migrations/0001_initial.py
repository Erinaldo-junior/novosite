# Generated by Django 5.0.7 on 2024-08-31 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=200)),
                ('disciplina', models.CharField(max_length=200)),
                ('nota_atividades', models.IntegerField(default=0)),
                ('nota_trabalho', models.IntegerField(default=0)),
                ('nota_prova', models.IntegerField(default=0)),
                ('media', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
