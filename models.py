from django.db import models


#Abstract class
class Recently(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def update_recent(self):
        """
        return True if is updated recently
        """
        return (datetime.now() - self.updated).days < 30

    def created_recent(self):
        """
        return True if is created recently
        """
        return (datetime.now() - self.created).days < 30

    class Meta:
        abstract = True

# Create your models here.
class Langue(models.Model):
    name = models.CharField(max_length=5, primary_key=True)

    def __str__(self):
        return self.name


class Application(Recently):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    priority = models.IntegerField()
    working = models.BooleanField()


    def __str__(self):
        return self.name



class Image(Recently):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    langue = models.ForeignKey(
             'Langue',
              on_delete=models.CASCADE,)
    application = models.ForeignKey(
             'Application',
              on_delete=models.CASCADE,)
    typeimage = models.ForeignKey(
           'SectionImage',
           on_delete=models.CASCADE,)

    def __str__(self):
        return self.name



class SectionImage(Recently):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name
