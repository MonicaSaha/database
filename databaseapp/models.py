from django.db import models


# Create your models here.

class Category(models.Model):
    Category_Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000)
    Discription = models.CharField(max_length=5000,default=' ')

    def __str__(self):
        return self.Title


class Product(models.Model):

    categories= models.ForeignKey(Category,on_delete=models.CASCADE)
    Product_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="image", default=" ")
    Discount = models.IntegerField(default=0)
    Price = models.IntegerField(default=0)
    Discription = models.CharField(max_length=5000)
    Type = models.CharField(max_length=100)
    Key_Features = models.CharField(max_length=5000)
    url=models.URLField(max_length=5000, default=' ')

    def __str__(self):
        return self.Name




class Specification(models.Model):

    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Specification_Id = models.AutoField(primary_key=True)
    Brand = models.CharField(max_length=100)
    Warranty = models.IntegerField(default=0)
    Batteries_no = models.IntegerField(default=0)
    Weight = models.IntegerField(default=0)
    Depth = models.IntegerField(default=0)
    Battery_Type = models.CharField(max_length=500)
    Color = models.CharField(max_length=500)
    Package_Content = models.CharField(max_length=5000)
    Accuracy = models.DecimalField( max_digits=50, decimal_places=5)
    Weighing_Capacity = models.IntegerField(default=0)
    Display_Size= models.IntegerField(default=0)
    Height = models.IntegerField(default=0)
    Width = models.IntegerField(default=0)
    Diameter = models.IntegerField(default=0)
    Display_Type = models.CharField(max_length=500)


    def __str__(self):
        return self.Brand

