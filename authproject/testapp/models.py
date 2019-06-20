from django.db import models
class gadi(models.Model):
	username=models.CharField(max_length=30)
	gadicompanyname=models.CharField(max_length=30)
	gadiname=models.CharField(max_length=30)
	gadino=models.CharField(max_length=30)
	phoneno=models.IntegerField()
