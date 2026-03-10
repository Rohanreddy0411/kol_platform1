from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

class KolProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    niche = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    followers = models.IntegerField(default=0)
    rating = models.FloatField(default=0)

class CompanyProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Campaign(models.Model):
    company = models.ForeignKey(CompanyProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.IntegerField()
    deadline = models.DateField()
    platform = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Wallet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    pending = models.IntegerField(default=0)

class Message(models.Model):
    sender = models.IntegerField()
    receiver = models.IntegerField()
    message = models.TextField()