from django.db import models
from django.forms import ModelForm
# Create your models here.
class Line(models.Model):
	LineCode=models.CharField(max_length=10)

	def __str__(self):
		return self.LineCode

	class Meta:
		ordering=['-LineCode']

class Machine(models.Model):
	MachineCode=models.CharField(max_length=10)
	FromLine=models.ForeignKey('Line',on_delete=models.CASCADE)

	def __str__(self):
		return self.MachineCode
	class Meta:
		ordering=['-MachineCode']

class Product(models.Model):
	ProductCode=models.CharField(max_length=20)
	FromMachine=models.ForeignKey('Machine',on_delete=models.CASCADE)
	ProductCT=models.CharField(max_length=20,default=1)
	Product_OEE=models.FloatField(max_length=10,default=0)
	Product_OEELoss=models.FloatField(max_length=10,default=0)
	Product_Yield=models.FloatField(max_length=10,default=0)

	def __str__(self):
		return self.ProductCode
	class Meta:
		ordering=['-ProductCode']

class Operation(models.Model):
	OptDateTime=models.DateTimeField(auto_now_add=True, blank=True)
	OptLine=models.ForeignKey('Line',on_delete=models.CASCADE,default=1)
	OptMachine=models.ForeignKey('Machine',on_delete=models.CASCADE,default=11)
	OptProductCode=models.CharField(max_length=20,default=0)
	OptConsum=models.CharField(max_length=20)
	OptGood=models.CharField(max_length=20)
	OptScraps=models.CharField(max_length=20)
	OptDownTime=models.CharField(max_length=20,default=0)
	OptDuration=models.CharField(max_length=20)

	class Meta:
		ordering=['-OptDateTime']
