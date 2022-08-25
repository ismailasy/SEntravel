from django.db import models

# Create your models here.
class Destination(models.Model):
    pays = models.CharField(max_length=50)
    photo =models.URLField(max_length=4000)

    def __str__(self):
        return self.pays

class Excursion(models.Model):
    nom= models.CharField(max_length=200)
    optionnelle =models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Voyage(models.Model):
    nom = models.CharField(max_length=100)
    duree =models.IntegerField(null=True)
    photo = models.URLField(max_length=5000)
    prix =models.FloatField()
    destination =models.ForeignKey(Destination,on_delete=models.CASCADE)
    excursions =models.ManyToManyField(Excursion,related_name='voyages',blank=True) 

    def __str__(self):
        return self.nom


class Client(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=30)

    def __str__(self):
        return self.nom +self.prenom 


class Reservation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    traitement = models.BooleanField(default=False)
    client =models.ForeignKey(Client,on_delete=models.CASCADE)
    voyage =models.ForeignKey(Voyage,on_delete=models.CASCADE)

    def __str__(self):
        return self.client.nom



    


