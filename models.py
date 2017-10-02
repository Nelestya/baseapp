from django.db import models

# Create your models here.

class Langue(models.Model):
    name = models.CharField(max_length=5, primary_key=True)
    
    def __str__(self):
        return self.name
    
    
class Application(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    date_pub = models.DateTimeField()
    priority = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
class ApiConnect(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    code = models.TextField()

    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=70)
    date_pub = models.DateTimeField()
    path = models.CharField(max_length=30)
    langue = models.ForeignKey(
             'Langue',
              on_delete=models.CASCADE,)
    application = models.ForeignKey(
             'Application',
              on_delete=models.CASCADE,)
    typeimage = models.ForeignKey(
           'TypeImage',
           on_delete=models.CASCADE,)
    
    def est_recent(self):

        """ Retourne True si l'article a ete publie dans

            les 30 derniers jours """

        return (datetime.now() - self.date_pub).days < 30


    

class TypeImage(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    
    
    
    def __str__(self):
        return self.name