from django.db import models

# Create your models here.
class User(models.Model):
    
    user_type=models.TextField()
    fname=models.TextField()
    lname=models.TextField()
    pwd=models.TextField()
    email=models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.email
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name+" - "+self.email

class Add_job(models.Model):
    company=models.ForeignKey(User,on_delete=models.CASCADE)
    keyword=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.company.fname+" "+self.keyword


class Apply(models.Model):
    fullname=models.TextField()
    email=models.EmailField(max_length=254)
    number=models.PositiveIntegerField()
    file=models.ImageField(upload_to='profile/',default="")

    def __str__(self):
        return self.fullname