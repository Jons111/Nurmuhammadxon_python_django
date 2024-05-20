from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    Name = models.CharField(max_length=40)
    turi = models.ForeignKey(Type, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    deadline = models.DateField(null=True, blank=True)
    project_url = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    dare = models.DateTimeField(auto_now=True)


class Team(models.Model):
    name = models.CharField(max_length=50)
    ishi = models.CharField(max_length=100)
    Text = models.TextField(null=True, blank=True)
    Rasm = models.ImageField(upload_to="media")
    twit_link = models.CharField(max_length=200, null=True, blank=True)
    face_link = models.CharField(max_length=200, null=True, blank=True)
    insta_link = models.CharField(max_length=200, null=True, blank=True)
    in_link = models.CharField(max_length=200, null=True, blank=True)


class Services(models.Model):
    ism = models.CharField(max_length=50)
    chizma = models.ImageField(upload_to='media')
    text = models.TextField(null=True, blank=True)


class Contact(models.Model):
    Ism = models.CharField(max_length=70)
    email = models.EmailField(max_length=90)
    subject = models.CharField(max_length=70)
    matn = models.TextField()
    created_at = models.DateField(auto_now=True)


class Subscribe(models.Model):
    Email = models.EmailField(max_length=70)
