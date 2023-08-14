from django.db import models
from control_user.models import Utilisateur

class Artiste(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Evenement(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_heure = models.DateTimeField()
    duree = models.DurationField()
    lieu = models.CharField(max_length=255)
    artistes = models.ManyToManyField(Artiste)

    def __str__(self):
        return self.titre
    
class Programme(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)  
    horaire = models.DateTimeField()
    artistes = models.ManyToManyField(Artiste)

    def __str__(self):
        return f"Programme de {self.evenement.titre} à {self.horaire}"
    
class StreamingEnDirect(models.Model):
    evenement = models.OneToOneField(Evenement, on_delete=models.CASCADE)
    lien_streaming = models.URLField()
    est_payant = models.BooleanField(default=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Streaming en direct de {self.evenement.titre}"
    

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               