from django.db import models

from evenement.models import Evenement  
from control_user.models import Utilisateur  

class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    nombre_billets = models.PositiveIntegerField()
    cout_total = models.DecimalField(max_digits=10, decimal_places=2)
    statut_paiement = models.BooleanField(default=False)

    def __str__(self):
        return f"Réservation de {self.utilisateur.username} pour {self.evenement.titre}"
    

class Paiement(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    mode_paiement = models.CharField(max_length=100)  
    transaction_reussie = models.BooleanField(default=False)
    date_paiement = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return f"Paiement pour la réservation {self.reservation.id}"