# Generated by Django 4.0.4 on 2022-05-07 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personne', '0001_initial'),
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referanceCmd', models.CharField(max_length=50)),
                ('dateCmd', models.DateField()),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personne.personne')),
                ('produits', models.ManyToManyField(to='produit.produit')),
            ],
            options={
                'ordering': ['referanceCmd'],
            },
        ),
    ]
