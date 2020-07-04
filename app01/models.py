from django.db import models

# Create your models here.

class Grades(models.Model):#继承类
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'grades'
        ordering = ['id']

class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    #关联外键,在学生表里定义外键，即班级表的主键
    sgrade = models.ForeignKey('Grades',on_delete=models.CASCADE)
    class Meta:
        db_table = 'students'
        ordering = ['id']

