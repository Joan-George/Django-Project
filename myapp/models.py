from django.db import models
from phone_field import PhoneField
import uuid
# Create your models here.

class Register(models.Model):
    """
    Description: Model Description
    """
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    C_Password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table="Register"

Gender=(('Male','Male'),('Female','Female'))

class BasicInformation(models.Model):
    """
    Description: Model Description
    """
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    Uid = models.IntegerField()
    Name = models.CharField( max_length=50)
    DOB = models.DateField()
    Gender = models.CharField( max_length=50,choices=Gender, default='Male')
    JoinedDate=models.DateField()
    Email = models.EmailField(unique=True)
    MobileNo = models.CharField(max_length=13)
    Address = models.TextField()


    class Meta:
        db_table="BasicInformation"

class Responsibility(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    Uid = models.IntegerField()
    Responsible = models.CharField( max_length=100)

    class Meta:
        db_table="Responsibility"

class Achivements(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    Uid = models.IntegerField()
    Achivement=models.CharField(max_length=200)

    class Meta:
        db_table="Achivements"

class Talents(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    Uid = models.IntegerField()
    Skills = models.CharField( max_length=50)

    class Meta:
        db_table="Talent"

class Exam(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    Uid=models.IntegerField()
    ExamName = models.CharField(max_length=50)

    class Meta:
        db_table="Exam"

class WorkingDetails(models.Model):
    """
    Description: Model Description
    """
    
    id = models.AutoField(primary_key=True)
    Uid = models.IntegerField()
    CompanyName = models.CharField(max_length=100,blank=True)
    Designation = models.CharField(max_length=100,blank=True)
    JoinedDate = models.DateField(blank=True,null=True)
    DismissalDate = models.DateField(blank=True)
    Address = models.TextField(blank=True)

    class Meta:
        db_table="WorkingDetails"

class EducationQualification(models.Model):
    id = models.AutoField(primary_key=True)
    Uid = models.IntegerField()
    StudiedAt = models.CharField(max_length=100)
    CourseName = models.CharField(max_length=100)

    class Meta:
        db_table="EducationQualification"

class AdminRegister(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    C_Password = models.CharField(max_length=100)

    class Meta:
        db_table="AdminRegister"
    