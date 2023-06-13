from django.contrib import admin
from .models import customer,purchase,SalesDetail,MassageChair,Branch,KPI,Salesperson, SalesTarget, Coupon, CouponUsage, Attendance,EXM


# @admin.register(customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('CID','CName','CStage','CAge_range','CGender','COccupation_category','CDemand_description','CHow','BID','CMON')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('MID', 'MNAME','PCost','PDate','MFuction', 'PAmount','MClass')

class SalesDetailAdmin(admin.ModelAdmin):
    list_display = ('MID', 'MNAME', 'SPrice', 'CID', 'CAge_range', 'SAmount','MClass')

class MassageChairAdmin(admin.ModelAdmin):
    list_display = ('MID', 'MNAME', 'MCost', 'MPrice','MState', 'MFuction', 'MAmount','MClass')
    
class BranchAdmin(admin.ModelAdmin):
    list_display = ('BID','BName', 'SID','SMON', 'SAc',"STc",'SNew','SOld','SOSALE','SNSALE')

class KPIAdmin(admin.ModelAdmin):
    list_display = ('KID', 'KName', 'KSet', 'KReach')

class SalespersonAdmin(admin.ModelAdmin):
    list_display = ['SID', 'SQ', 'SR', 'STQ']

class SalesTargetAdmin(admin.ModelAdmin):
    list_display = ['TID', 'BID', 'SID', 'TSet', 'TReach', 'TSetdate', 'TDeadline']

class CouponAdmin(admin.ModelAdmin):
    list_display = ['AID', 'AName', 'AContent', 'AUse', 'ADeadline']

class CouponUsageAdmin(admin.ModelAdmin):
    list_display = ['AID', 'CID', 'AUsedate']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['SID', 'date', 'SW', 'SG', 'SL']

class EXMAdmin(admin.ModelAdmin):
    list_display = ['MID', 'MNAME', 'MFuction', 'EXMAmount','MClass']

# Register your models here.
admin.site.register(customer,CustomerAdmin)
admin.site.register(purchase, PurchaseAdmin)
admin.site.register(SalesDetail, SalesDetailAdmin)
admin.site.register(MassageChair, MassageChairAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(KPI, KPIAdmin)
admin.site.register(Salesperson,SalespersonAdmin)
admin.site.register(SalesTarget,SalesTargetAdmin)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(CouponUsage,CouponUsageAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(EXM,EXMAdmin)

