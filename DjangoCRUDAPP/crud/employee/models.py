from django.db import models  

class Employee(models.Model):  
    edepartment = models.CharField(max_length=20)  
    efirstname = models.CharField(max_length=100)
    elastname = models.CharField(max_length=100)  
    eemail = models.EmailField() 
    econtact = models.CharField(max_length=15) 

    def __str__(self):
        return "%s " %(self.edepartment) 
    class Meta:  
        db_table = "employee"  