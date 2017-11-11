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



class Application(Recently):
    name = models.CharField(max_length=30, primary_key=True)
    priority = models.IntegerField()
    working = models.BooleanField()


    def __str__(self):
        return self.name



class Image(Recently):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
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
    

class BugReport(Recently):
    STATUS_CHOICE = (
    ('published', 'Published'),
    ('resolved', 'Resolved'),
    )
    title = models.CharField(max_length=50)
    mail = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='published')

    def __str__(self):
        return self.title

class ContactUs(Recently):
    STATUS_CHOICE = (
    ('read', 'Read'),
    ('unread', 'Unread'),
    )
    title = models.CharField(max_length=50)
    mail = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='unread')

    def __str__(self):
        return self.title
