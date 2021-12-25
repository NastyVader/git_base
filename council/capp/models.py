from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator

# Create your models here.

class StudentProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    S_ID = models.CharField(primary_key=True, max_length=10,
                            validators=[
                                RegexValidator(regex='^1VE\d\d\w\w\d\d\d',
                                                message='Invalid',code='Invalid')]
                            )
    S_NAME = models.CharField(max_length=30)
    S_DOB = models.DateField()
    S_SEM = models.IntegerField()
    S_SEC = models.CharField(max_length=1)
    S_DEP = models.CharField(max_length=3)
    S_PIC = models.ImageField(upload_to="capp/profile_pic",blank=True)


    def __str__(self):
        return self.S_ID

class Union(models.Model):
    
    head = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    UNION_ID = models.CharField(max_length=2,primary_key=True)
    UNION_NAME = models.CharField(max_length=25)

    def __str__(self):
        return self.UNION_ID

class UnionForm(models.Model):

    head = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    UNION_ID = models.CharField(max_length=2,primary_key=True)
    UNION_NAME = models.CharField(max_length=25)
    M1 = models.CharField(max_length=10,
                            validators=[
                                RegexValidator(regex='^1VE\d\d\w\w\d\d\d',
                                                message='Invalid',code='Invalid')]
                         )
    M2 = models.CharField(max_length=10,
                            validators=[
                                RegexValidator(regex='^1VE\d\d\w\w\d\d\d',
                                                message='Invalid',code='Invalid')]
                         )
    M3 =models.CharField(max_length=10,
                            validators=[
                                RegexValidator(regex='^1VE\d\d\w\w\d\d\d',
                                                message='Invalid',code='Invalid')]
                         )
    M4 = models.CharField( max_length=10,
                            validators=[
                                RegexValidator(regex='^1VE\d\d\w\w\d\d\d',
                                                message='Invalid',code='Invalid')]
                         )
    M5 = models.CharField(max_length=10,
                            validators=[
                                RegexValidator(regex='^1VE\d\d\w\w\d\d\d',
                                                message='Invalid',code='Invalid')]
                         )

    def __str__(self):
        return self.UNION_NAME

class Candidate(models.Model):

    USN = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    U_NAME = models.CharField(max_length=25,null=True)
    def __str__(self):
        return str(self.USN)

