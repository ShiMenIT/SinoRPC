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
	LineCode=models.ForeignKey('Line',on_delete=models.CASCADE,related_name="Machine",verbose_name = u'Line')

	def __str__(self):
		return self.MachineCode
	class Meta:
		ordering=['-MachineCode']

class Product(models.Model):
	ProductCode=models.CharField(max_length=20)
	MachineCode=models.ForeignKey('Machine',on_delete=models.CASCADE,related_name="Product",verbose_name = u'Machine',null = True, blank = True)
	ProductCT=models.CharField(max_length=20,default=1)

	def __str__(self):
		return self.ProductCode
	class Meta:
		ordering=['-ProductCode']

class Operation(models.Model):
	LineCode=models.ForeignKey('Line',null = True, blank = True,related_name="Operation",verbose_name = u'Line')
	MachineCode=models.ForeignKey('Machine',null = True, blank = True,related_name="Operation",verbose_name = u'Machine')
	ProductCode = models.ForeignKey('Product', null = True, blank = True,related_name="Operation",verbose_name = u'Product')
	DateTime=models.DateTimeField(auto_now_add=False, blank=True) 
	Consum=models.CharField(max_length=20)
	Good=models.CharField(max_length=20)
	Scraps=models.CharField(max_length=20)
	Duration=models.CharField(max_length=20)
	DownTime=models.CharField(max_length=20,null = True, blank = True,)

	class Meta:
		ordering=['-DateTime']

#creat ModelForm
class OperationForm(ModelForm):
	class Meta:
		model=Operation
		#fields='__all__'
		fields=('LineCode', 'MachineCode', 'ProductCode')

