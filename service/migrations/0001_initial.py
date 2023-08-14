# Generated by Django 4.0.10 on 2023-07-18 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evenement', '0002_streamingendirect_programme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_service', models.CharField(choices=[('spot_publicitaire', 'Spot publicitaire'), ('demande_chanson', 'Demande de chanson')], max_length=20)),
                ('duree_spot_publicitaire', models.DurationField(blank=True, null=True)),
                ('texte_spot_publicitaire', models.TextField(blank=True, null=True)),
                ('lien_chanson_demandee', models.URLField(blank=True, null=True)),
                ('accepte', models.BooleanField(default=False)),
                ('date_demande', models.DateTimeField(auto_now_add=True)),
                ('date_acceptation', models.DateTimeField(blank=True, null=True)),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evenement.evenement')),
            ],
        ),
    ]