from django.db import models
import datetime
class reg_form(models.Model):
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
class login(models.Model):
    username = models.CharField(max_length=100)
    passw=models.CharField(max_length=100)
    uid=models.ForeignKey('reg_form',on_delete=models.CASCADE)
    utype=models.CharField(max_length=50)
class productad(models.Model):
    prname=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.FileField(upload_to='file')
    description=models.CharField(max_length=500)
class cart(models.Model):
    uid = models.ForeignKey('reg_form', on_delete=models.CASCADE)
    date = models.DateTimeField()
    pid = models.ForeignKey('productad', on_delete=models.CASCADE)
    qty = models.IntegerField()
    total = models.FloatField()
class ordermaster(models.Model):
    uid=models.ForeignKey('reg_form',on_delete=models.CASCADE)
    date=models.DateTimeField()
    total=models.FloatField()
class orderchild(models.Model):
    oid=models.ForeignKey('ordermaster',on_delete=models.CASCADE)
    pid=models.ForeignKey('productad',on_delete=models.CASCADE)
    qty = models.IntegerField()
    total=models.FloatField()
    status=models.CharField(max_length=10)

