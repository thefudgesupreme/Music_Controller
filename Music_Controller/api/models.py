from django.db import models,connection
import uuid
# Create your models here.


def get_uuid():
    code = str(uuid.uuid4().hex).upper
    return code

class Room(models.Model):
    code = models.CharField(max_length= 6, default="", unique=True)


    

        
