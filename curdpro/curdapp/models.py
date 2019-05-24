from django.db import models

class ProductData(models.Model):
    mproduct_id=models.IntegerField()
    mproduct_name=models.CharField(max_length=50)
    mproduct_cost=models.IntegerField()
    mproduct_color=models.CharField(max_length=50)
    mproduct_class=models.CharField(max_length=10)
    mnumber_of_products=models.IntegerField()
    mcustomer_name=models.CharField(max_length=50)
    mmobile_number=models.BigIntegerField()
    memail=models.EmailField(max_length=50)
