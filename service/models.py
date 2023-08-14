from django.db import models

from evenement.models import Evenement  

class Service(models.Model):
    TYPE_CHOICES = (
        ('spot_publicitaire', 'Spot publicitaire'),
        ('demande_chanson', 'Demande de chanson'),
    )

    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    type_service = models.CharField(max_length=20, choices=TYPE_CHOICES)
    duree_spot_publicitaire = models.DurationField(null=True, blank=True)
    texte_spot_publicitaire = models.TextField(null=True, blank=True)
    lien_chanson_demandee = models.URLField(null=True, blank=True)
    accepte = models.BooleanField(default=False)
    date_demande = models.DateTimeField(auto_now_add=True)
    date_acceptation = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_service_display()} pour {self.evenement.titre}"