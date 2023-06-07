from django.contrib import admin
from .models import customer,purchase,SalesDetail,MassageChair,Branch,KPI,Salesperson, SalesTarget, Coupon, CouponUsage, Attendance


# @admin.register(customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('CID','CName','CEmail','CStage','CActrecord','CStartdate','CDealdate','SID','CDemand_description','CSpecial_requests','CAge_range','COccupation_category')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('PID', 'BID', 'MID', 'PCost', 'PAmount')

class SalesDetailAdmin(admin.ModelAdmin):
    list_display = ('BID', 'SID', 'CID', 'MID', 'SAmount', 'SPrice', 'SDiscount', 'SPay', 'SDate', 'SRepurchase', 'SPayment')

class MassageChairAdmin(admin.ModelAdmin):
    list_display = ('MID', 'MState', 'PID', 'BID', 'MPrice', 'MCost', 'MAmount', 'MClass')
    
class BranchAdmin(admin.ModelAdmin):
    list_display = ('BID', 'SID', 'SAc')

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

