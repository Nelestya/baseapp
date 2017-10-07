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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    priority = models.IntegerField()


    def __str__(self):
        return self.name

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

class ApiConnect(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    code = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
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

    def __str__(self):
        return self.name



class SectionImage(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
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

    def __str__(self):
        return self.name
