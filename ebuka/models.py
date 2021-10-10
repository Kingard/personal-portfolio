# from functools import _Descriptor
from django.db import models
from django.db.models.deletion import CASCADE

# Home section 

class Home(models.Model):
    name = models.CharField(max_length=30)
    greeting_1 = models.CharField(max_length=10)
    greeting_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to = 'picture/')

    # Save time stamp (instace) when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# About section

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    # Update modification time
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                              on_delete=models.CASCADE)
    social_name = models.CharField(max_length=15)
    link = models.URLField(max_length=200)



# skills section

class Category(models.Model):
    name = models.CharField(max_length=20) 

    update = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Skills(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)


# Portfolio section

class Portfolio(models.Model):
    image = models.ImageField(upload_to ='portfolio/')
    link = models.URLField(max_length=200)
    description = models.TextField(max_length=300,blank=False)


    def __str__(self):
        return f'Portfolio{self.id}'