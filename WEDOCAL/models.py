from django.db import models
from django.utils import timezone
from datetime import date


class Patient(models.Model):
    name = models.CharField(max_length=100)
    cin = models.CharField(max_length=20,unique=True)
    adding_date = models.DateTimeField(default=timezone.now)
    birthdefaulte = date(1900,1,1)
    birthdate = models.DateField(default=birthdefaulte)
    v6 = models.CharField(max_length=2,choices=(('GG','GG'),('GA','GA'),('AA','AA')))
    v7 = models.CharField(max_length=2,choices =(('CC','CC'),('CT','CT'),('TT','TT')))
    haplo = models.CharField(max_length=2,choices = (('1/1','1/1'),('1/2','1/2'),('1/3','1/3'),('2/2','2/2'),('2/3','2/3')))
    def age (self):
        birthDate = self.birthdate
        today = date.today()
        age =  today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age
    def dose(self):
        age = self.age()
        dic = {'GG':1,'GA':2,'AA':3,'CC':1,'CT':2,'TT':3,'1/1':1,'1/2':2,'1/3':2,'2/2':3,'2/3':3}
        do = 10**(1.925-(0.108*dic[self.v6])-(0.073*dic[self.v7])-(0.093*dic[self.haplo])-(0.003*age))
        return round(do,3)
class Dose(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    dose_value = models.DecimalField(max_digits=10,decimal_places=3)
    dose_date = models.DateField(default=timezone.now)
    comment = models.TextField(max_length=1000,default='nothing')
    commenter = models.CharField(max_length=20,choices=(('Moi','Moi'),('Mon Medecin','Mon Medecin'),('Un Proche','Un Proche')))
