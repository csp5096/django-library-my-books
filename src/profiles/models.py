from django.db import models

class Profiles(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='Please Enter The User Description Here')
    # locations = models.CharField(max_length=120, default="My Location Default", blank=True, null=True)
    # job = models.CharField(max_length=120, null=True)

    def __unicode__(self):
        return self.name
