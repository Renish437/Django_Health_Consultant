from django.db import models

# Create your models here.

class TopNavbar(models.Model):
    phone_no = models.CharField(max_length=15,unique=True,default=9888744860)
    email = models.EmailField(unique=True,default='xyz@gmail.com')
    facebook_link = models.URLField(max_length=200,blank=True,null=True)
    insta_link = models.URLField(max_length=200,blank=True,null=True)
    whatsapp_link = models.URLField(max_length=200,blank=True,null=True)
    linkedin_link =  models.URLField(max_length=200,blank=True,null=True)
    twitter_link =  models.URLField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return f"{self.phone_no} {self.email}" 
    
    