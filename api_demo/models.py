from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    lib_id = models.CharField(db_column='Lib_Id', max_length = 20, null=False)
    name = models.CharField(db_column='Name', max_length = 500, null=False)
    sem = models.IntegerField(db_column='Sem', max_length=10, null=False)
    branch = models.CharField(db_column='Branch', max_length=100, null=False)
    course = models.CharField(db_column='Course', max_length=100, null=False) 
    roll_no = models.CharField(db_column='Roll No', max_length=100, null=False)

# class Employee(models.Model):
#     id = models.AutoField(db_column='id', primary_key=True)
#     emp_id = models.IntegerField(db_column='Emp_Id', max_length=100, null=False)

class MarkAttendance(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    # emp_id = models.ForeignKey(Employee, db_column='Emp_Id', on_delete= models.SET_NULL, max_length = 20)         
    lib_id = models.CharField(db_column = 'Lib_Id', max_length=50)
    status = models.CharField(db_column='Status', max_length =100, default='INSERT', null=False)
    result = models.CharField(db_column = 'result', max_length = 50, null=False)
