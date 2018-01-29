from django.db import models

# Create your models here.
class Line(models.Model):
	LineCode=models.CharField(max_length=10)

	def __str__(self):
		return self.LineCode

class Machine(models.Model):
	MachineCode=models.CharField(max_length=10)
	FromLine=models.ForeignKey('Line',on_delete=models.CASCADE)

	def __str__(self):
		return self.MachineCode

class Product(models.Model):
	ProductCode=models.CharField(max_length=20)
	FromMachine=models.ForeignKey('Machine',on_delete=models.CASCADE)
	ProductCT=models.CharField(max_length=20,default=1)
	Product_OEE=models.FloatField(max_length=10,default=0)
	Product_OEELoss=models.FloatField(max_length=10,default=0)
	Product_Yield=models.FloatField(max_length=10,default=0)

	def __str__(self):
		return self.ProductCode

class Operation(models.Model):
	OptDateTime=models.DateTimeField(auto_now_add=True, blank=True)
	OptLine=models.ForeignKey('Line',on_delete=models.CASCADE,default=1)
	OptMachine=models.ForeignKey('Machine',on_delete=models.CASCADE,default=11)
	OptProduct=models.ForeignKey('Product',on_delete=models.CASCADE,default=111)
	OptConsum=models.CharField(max_length=20)
	OptGood=models.CharField(max_length=20)
	OptScraps=models.CharField(max_length=20)
	OptDuration=models.CharField(max_length=20)
