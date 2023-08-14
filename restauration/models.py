from django.db import models

class Restauration(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En attente'),
        ('confirme', 'Confirmé'),
        ('preparation', 'En préparation'),
        ('livre', 'Livrée'),
        ('retire', 'Retirée'),
    )

    menu_du_jour = models.TextField()
    plat = models.CharField(max_length=100)
    description = models.TextField()
    option_vegetarien = models.BooleanField(default=False)
    option_vegan = models.BooleanField(default=False)
    image = models.ImageField(upload_to='menu_images/')
    option_livraison = models.BooleanField(default=False)
    adresse_livraison = models.TextField(null=True, blank=True)
    horaires_retrait = models.CharField(max_length=100, null=True, blank=True)
    quantite = models.PositiveIntegerField(default=1)
    preferences_speciales = models.TextField(null=True, blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_reservation = models.DateTimeField(auto_now_add=True)
    date_livraison = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Restauration de {self.plat} - {self.date_reservation}"