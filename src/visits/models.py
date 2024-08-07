from django.db import models

class PageVisit(models.Model):
    # id -> hidden -> primary key -> autofield -> 1,2,3,4,5
    path = models.TextField(blank=True,null=True) #col
    timestamp = models.DateTimeField(auto_now_add=True)   #col

