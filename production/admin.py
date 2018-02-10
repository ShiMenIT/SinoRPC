from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Line)
admin.site.register(Machine)
admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('ProductCode', 'FromMachine','Product_OEE','Product_Yield')
# admin.site.register(Product, ProductAdmin)

class OperationAdmin(admin.ModelAdmin):
	list_display = ('LineCode','MachineCode','ProductCode','DateTime','Consum','Good','Scraps','Duration','DownTime')
admin.site.register(Operation,OperationAdmin)