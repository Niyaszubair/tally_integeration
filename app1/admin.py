from django.contrib import admin
from app1.models import *

# Register your models here.
@admin.register(purchase_model)
class purchase_admin(admin.ModelAdmin):
    list_display = ('id','comp','itm','name','qnt','brate','bvalue','addcost','totalvalue')

@admin.register(sale_model)
class sale_admin(admin.ModelAdmin):
    list_display = ('id','comp','itm','name','qnt','brate','bvalue','addcost','totalvalue')

@admin.register(analysis_view)
class analysis_admin(admin.ModelAdmin):
    list_display = ('id','comp','particular','iquantity','ieff_rate','ivalue','oquantity','oeff_rate','ovalue')

@admin.register(groupanalysismodel)
class grpanalisysadmin(admin.ModelAdmin):
    list_display = ('id','comp','pert','perticular','pquatity','prate','pvalue','squatity','srate','svalue')

@admin.register(salevouchermodel)
class salevoucheradmin(admin.ModelAdmin):
    list_display = ('id','comp','stockitem','udergroup','date','name','quantity','basicrate','basicvalue','addlcost','totalvalue','efsrate')

@admin.register(purchasevouchermodel)
class purchasevoucheradmin(admin.ModelAdmin):
    list_display = ('id','comp','stockitem','udergroup','date','name','quantity','basicrate','basicvalue','addlcost','totalvalue','efsrate')

@admin.register(countrymodel)
class countryadmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(statemodel)
class stateadmin(admin.ModelAdmin):
    list_display = ('id','cname','sname')

@admin.register(ledgeranalysismodel)
class ledgeranalisysadmin(admin.ModelAdmin):
    list_display = ('id','lpert','lperticular','lpquatity','lprate','lpvalue','lsquatity','lsrate','svalue')

@admin.register(purchaseledgervouchermodel)
class purchaseledgervoucheradmin(admin.ModelAdmin):
    list_display = ('id','lstockitem','ludergroup','ldate','lname','lquantity','lbasicrate','lbasicvalue','laddlcost','ltotalvalue','lefsrate')

@admin.register(salesledgervouchermodel)
class salesledgervoucheradmin(admin.ModelAdmin):
    list_display = ('id','lstockitem','ludergroup','ldate','lname','lquantity','lbasicrate','lbasicvalue','laddlcost','ltotalvalue','lefsrate')
