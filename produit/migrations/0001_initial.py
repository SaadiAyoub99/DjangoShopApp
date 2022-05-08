# Generated by Django 4.0.4 on 2022-05-07 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produitRef', models.CharField(max_length=50)),
                ('nomProduit', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('image', models.CharField(max_length=5000, null=True)),
                ('dateProduit', models.DateField()),
                ('prix', models.FloatField(max_length=50)),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorie.categorie')),
            ],
            options={
                'ordering': ['produitRef'],
            },
        ),
    ]
