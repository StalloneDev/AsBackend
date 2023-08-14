# Generated by Django 4.0.10 on 2023-07-18 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evenement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamingEnDirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien_streaming', models.URLField()),
                ('est_payant', models.BooleanField(default=False)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('evenement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evenement.evenement')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaire', models.DateTimeField()),
                ('artistes', models.ManyToManyField(to='evenement.artiste')),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evenement.evenement')),
            ],
        ),
    ]
