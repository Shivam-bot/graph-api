from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'School Name'

    def __str__(self):
        return self.school_name

class SClass(models.Model):
    standard = models.CharField(max_length=20)
    section = models.CharField(max_length=15)
    school = models.ForeignKey(School, on_delete = models.DO_NOTHING)

    class Meta:
        db_table = 'Standard'
    
    def __str__(self):
        return self.standard

class Strength(models.Model):
    strength = models.IntegerField()
    class_n  = models.ForeignKey(SClass, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "Strength"
    def __int__(self):
        return self.strength


class myUser(models.Model):
    
    objects = None
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    mobile_no = models.BigIntegerField()
    strength = models.ForeignKey(Strength, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'myUser'

    def __str__(self):
        return self.name
