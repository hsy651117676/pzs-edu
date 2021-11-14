from django.db import models

class regioncode(models.Model):
    id= models.CharField(max_length=12,primary_key=True)
    pid= models.CharField(max_length=12)
    text= models.CharField(max_length=255)
    allname= models.CharField(max_length=255)
    level= models.IntegerField()
    citycode= models.IntegerField()


