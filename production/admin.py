from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Line)
admin.site.register(Machine)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProductCode', 'FromMachine','Product_OEE','Product_Yield')
admin.site.register(Product, ProductAdmin)

class OperationAdmin(admin.ModelAdmin):
    list_display = ('OptDateTime','OptLine','OptMachine','OptProduct','OptConsum','OptGood','OptScraps','OptDuration')
admin.site.register(Operation, OperationAdmin)