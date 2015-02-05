from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=10, null=True)
    score = models.FloatField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=30)
    semester = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    teachers = models.ManyToManyField(Teacher, through='Course')
    
    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    score = models.FloatField()
    section = models.CharField(max_length=2)
    
    def __str__(self):
        return self.subject + " " + self.section