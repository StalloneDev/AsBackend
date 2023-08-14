from django.db import models
from control_user.models import Utilisateur, ProfilArtiste


class Discussion(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='discussions')
    artiste = models.ForeignKey(ProfilArtiste, on_delete=models.CASCADE, related_name='discussions')

    def __str__(self):
        return f"Discussion entre {self.utilisateur.username} et {self.artiste.nom_artiste}"
    
class Message(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='messages')
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.auteur.username} dans la discussion {self.discussion}"