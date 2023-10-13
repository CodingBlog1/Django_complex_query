from django.db import models

# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=20)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    visit_city = models.ManyToManyField(City,related_name='visitor')
    hometown=models.ForeignKey(City,on_delete=models.CASCADE,related_name='birth')
    living = models.ForeignKey(City,on_delete=models.CASCADE,related_name='citizen')
    
    def __str__(self):
        return self.first_name + self.last_name