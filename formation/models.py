from django.db import models


class Formation(models.Model):
    TYPE_CHOICES = (
        ('piano', 'Piano'),
        ('batterie', 'Batterie'),
        ('guitare', 'Guitare'),
        ('flute', 'Flûte'),
        ('danse', 'Danse'),
    )

    type_cours = models.CharField(max_length=20, choices=TYPE_CHOICES)
    horaires = models.CharField(max_length=100)
    duree = models.DurationField()
    disponibilite = models.BooleanField(default=True)
    cout = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_type_cours_display()} - {self.horaires}"