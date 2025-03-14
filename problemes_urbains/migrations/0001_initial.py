# Generated by Django 5.1.7 on 2025-03-14 10:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Probleme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('categorie', models.CharField(choices=[('denis', 'Dénis'), ('routes', 'Routes endommagées'), ('eau', "Coupures d'eau"), ('eclairage', 'Éclairage public'), ('autre', 'Autre')], max_length=20)),
                ('localisation', models.CharField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(default='nouveau', max_length=20)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
