from django.db import models,connection
import string, random
from django.utils.timezone import now
# Create your models here.


def get_random_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() > 0:
            break

    return code

class Room(models.Model):
    code = models.CharField(max_length= 8, default="", unique=True)
    host = models .CharField(max_length=50, default = "Joker",unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(default=now, editable=False)


    

        
