from django.db import models

# Create your models here.
class Company(models.Model):
    conmpany_id = models.AutoField(primary_key=True)
    name = models.CharField(
      'Name' ,  max_length=50 ,blank=False,null=False, default='name')

    description= models.CharField(
        "Info", max_length=50 , blank=False, null=False, default='name')

    new = models.CharField(max_length=200,blank=False,null=False,default='nw')   

    type = models.CharField(max_length=100,choices=(('IT','IT'),('Not it ','Not it'),('stocks','stocks')),default='name')
    
    added_date= models.DateField(
        auto_now=True
    
    )

    def __str__(self):
      return self.name
class Employees(models.Model):
    name= models.CharField(
        "Title", max_length=50 ,blank=False,null=False, default='name')

    address= models.CharField(
        "Street", max_length=50, blank=False,null=False, default='name'
    )

    position= models.CharField(
        "Title", max_length=50, blank=False,null=False, choices=(('manager','manager'),('Seniormanger','seniormanager'),('cheifofficer','cheifofficer')),default='name'
    )



    about= models.CharField(
        "Description", max_length=100, blank=False, null=False, default='name'
    )

    number= models.CharField(
        "Number", max_length=8, blank=False,null=False, default='name'
    )

    company = models.ForeignKey(Company,on_delete=models.CASCADE )