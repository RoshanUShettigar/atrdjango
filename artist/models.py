from django.db import models

# Create your models here.
class Artist(models.Model):
   # Artist_id=models.AutoField()
    Artist_name= models.CharField(max_length=50)
    Email= models.EmailField(max_length=50)
    Phone_no= models.IntegerField()

    def __str__(self):
        return self.Artist_name

class Articles(models.Model):
  pass