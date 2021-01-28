from django.db import models


class Mobile(models.Model):
    producer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.model


class Comment(models.Model):
    content = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

        
