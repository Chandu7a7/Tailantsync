from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    Course_name = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    Course_image = models.ImageField(null=True , blank=True)


    def __str__(self):
        return self.Course_name
    
    @property
    def imageURL(self):
        try:
            url=self.Course_image.url
        except:
            url=''
        return url