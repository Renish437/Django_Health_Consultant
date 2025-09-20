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
    
class About(models.Model):
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    our_mission = models.TextField()
    our_vision = models.TextField()
    image = models.ImageField(upload_to='images/about',null=True,blank=True)
    signature = models.ImageField(upload_to='images/about/signatures',null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
    
class Services(models.Model):
    logo = models.CharField(max_length=2555,null=True,blank=True)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    image = models.ImageField(upload_to='images/services/photos',null=True,blank=True)
    
    def __str__(self):
        return self.title

class Slider(models.Model):
    super_script = models.CharField(max_length=2555)
    title = models.CharField(max_length=2555)
    sub_script = models.TextField()
    image = models.ImageField(upload_to='sliders/images')
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
    
    