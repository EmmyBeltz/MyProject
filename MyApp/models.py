from django.db import models

# Create your models here.

class TheWebsiteInfo(models.Model):
   StudentsNumber = models.IntegerField() 
   CoursesNumber = models.IntegerField()
   EventsNumber = models.IntegerField()
   TrainersNumber = models.IntegerField()

class TheWebsiteAboutText(models.Model):
   about_txt = models.TextField(blank=True)

class TheWebsiteImages(models.Model):
   WebsiteImg = models.ImageField(upload_to='static/assets/img')

class TheWebsiteTrainers(models.Model):
   Name = models.CharField(max_length=70)
   Title = models.CharField(max_length=200)
   Desc = models.CharField(max_length=500)
   Social = models.URLField(blank=True)
   Image = models.ImageField(upload_to='static/assets/img/trainer',blank=True)

class TheWebsiteCourses(models.Model):
   Title = models.CharField(max_length=200)
   smalltitle = models.CharField(max_length=200,null=True,blank=True)
   Desc = models.CharField(max_length=500)
   Subjects = models.CharField(max_length=500)
   Image = models.ImageField(upload_to='static/assets/img/trainer/subjects',blank=True)
   BigImage = models.ImageField(upload_to='static/assets/img/trainer/subjects',blank=True)
   LongDescription = models.TextField(blank=True)

class TheWebsitePricing(models.Model):
   Title = models.CharField(max_length=100,blank=True)
   Money = models.CharField(max_length=100,blank=True)
   Freq = models.CharField(max_length=100,blank=True)
   Desc = models.CharField(max_length=500,blank=True)
   Crossed = models.CharField(max_length=500,blank=True)
   CourseTitle = models.CharField(max_length=200)

class TheWebsiteTestimonials(models.Model):
   Name = models.CharField(max_length=70, blank=True)
   Image = models.ImageField(upload_to='static/assets/img/testimony',blank=True)
   Title = models.CharField(max_length=200, blank=True)
   Saying = models.TextField(blank=True)
   Social = models.URLField(blank=True)