from django.db import models
from datetime import datetime
# Create your models here.
 
class Utilisateur(models.Model):
   nom_utilisateur = models.CharField(max_length=200)
   email = models.EmailField(max_length=100)
   mot_de_passe = models.CharField(max_length=200)
   adresse = models.CharField(max_length=200)




class Utilisateur_admin (Utilisateur):
   status = models.CharField(max_length=200)

class Utilisateur_privilégié (Utilisateur):
   status = models.CharField(max_length=200)

class Utilisateur_simple (Utilisateur):
   status = models.CharField(max_length=200)




class Rubrique (models.Model):
   nom_rub = models.CharField(max_length=200, unique=True)
   utilisateur_admin = models.ForeignKey(Utilisateur_admin, on_delete=models.CASCADE,null=True)

class Répertoire(models.Model):
    nom_rep = models.CharField(max_length=200)
    date_création = models.DateField(default = datetime.now()) 
    rubrique = models.ForeignKey(Rubrique, on_delete=models.CASCADE,null=True)

class Document (models.Model):
    nom_doc = models.CharField(max_length=200)
    taille = models.IntegerField()
    propriétaire = models.CharField(max_length=200)
    date_création = models.DateField(auto_now_add=True)
    emplacement = models.CharField(max_length=200)
    fichier = models.FileField(upload_to= 'doc/',null=True)
    répertoire = models.ForeignKey(Répertoire,on_delete=models.CASCADE,null=True)
    utilisateur_privilégié = models.ForeignKey(Utilisateur_privilégié, on_delete=models.CASCADE,null=True)
    utilisateurs = models.ManyToManyField(Utilisateur,related_name='documents', blank=False)
    def delete(self, *args, **kwargs):
      self.fichier.delete()
      super().delete(*args, **kwargs)
   

class Notification (models.Model):
    titre =  models.CharField(max_length=200)
    description =  models.CharField(max_length=100)
    date_envoie = models.DateField()
    utilisateur_simple = models.ForeignKey(Utilisateur_simple, on_delete=models.CASCADE,null=True)

