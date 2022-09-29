from django.db import models

# Create your models here.
class Course(models.Model):
    cource_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.cource_name


class Question(models.Model):
    course = models.ForeignKey(Course,on_delete= models.CASCADE)
    question  =models.CharField(max_length = 500,blank = True)
    question2  =models.ImageField(upload_to ='static/',blank = True)
    ans = models.IntegerField()
    option_1 = models.CharField(max_length = 250)
    option_2 = models.CharField(max_length = 250)
    option_3 = models.CharField(max_length = 250,blank = True)
    option_4 = models.CharField(max_length = 250,blank = True)
    
    def __str__(self):
        return self.question