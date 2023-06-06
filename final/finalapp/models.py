from django.db import models

class customer(models.Model):
    CID = models.CharField(max_length=20, unique=True)
    CName = models.CharField(max_length=100)
    CEmail = models.EmailField()
    CStage = models.CharField(max_length=50)
    CActrecord = models.TextField(blank=True)
    CStartdate = models.DateField()
    CDealdate = models.DateField(null=True, blank=True)
    SID = models.CharField(max_length=20)
    CDemand_description = models.TextField(blank=True)
    CSpecial_requests = models.TextField(blank=True)
    CAge_range = models.CharField(max_length=20)
    COccupation_category = models.CharField(max_length=50)

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class purchase(models.Model):
    PID = models.CharField(max_length=20)
    BID = models.CharField(max_length=20)
    MID = models.CharField(max_length=20)
    PCost = models.DecimalField(max_digits=10, decimal_places=2)
    PAmount = models.IntegerField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class SalesDetail(models.Model):
    BID = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    CID = models.CharField(max_length=20)
    MID = models.CharField(max_length=20)
    SAmount = models.IntegerField()
    SPrice = models.DecimalField(max_digits=10, decimal_places=2)
    SDiscount = models.DecimalField(max_digits=10, decimal_places=2)
    SPay = models.DecimalField(max_digits=10, decimal_places=2)
    SDate = models.DateField()
    SRepurchase = models.BooleanField()
    SPayment = models.CharField(max_length=50)

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class MassageChair(models.Model):
    MID = models.CharField(max_length=20)
    MState = models.CharField(max_length=50)
    PID = models.CharField(max_length=20)
    BID = models.CharField(max_length=20)
    MPrice = models.DecimalField(max_digits=10, decimal_places=2)
    MCost = models.DecimalField(max_digits=10, decimal_places=2)
    MAmount = models.IntegerField()
    MClass = models.CharField(max_length=50)

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class Branch(models.Model):
    BID = models.CharField(max_length=20)
    BName = models.CharField(max_length=20,null=True, blank=True)
    SID = models.CharField(max_length=20)
    SAc = models.IntegerField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class KPI(models.Model):
    KID = models.CharField(max_length=20, primary_key=True)
    KName = models.CharField(max_length=100)
    KSet = models.CharField(max_length=50)
    KReach = models.CharField(max_length=50)

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class Salesperson(models.Model):
    SID = models.CharField(max_length=20)
    SName = models.CharField(max_length=20,null=True, blank=True)
    SQ = models.IntegerField()
    SR = models.DecimalField(max_digits=10, decimal_places=2)
    STQ = models.IntegerField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class SalesTarget(models.Model):
    TID = models.CharField(max_length=20)
    BID = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    TSet = models.CharField(max_length=50)
    TReach = models.CharField(max_length=50)
    TSetdate = models.DateField()
    TDeadline = models.DateField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳


class Coupon(models.Model):
    AID = models.CharField(max_length=20)
    AName = models.CharField(max_length=100)
    AContent = models.TextField()
    AUse = models.BooleanField()
    ADeadline = models.DateField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳


class CouponUsage(models.Model):
    AID = models.CharField(max_length=20)
    CID = models.CharField(max_length=20)
    AUsedate = models.DateField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳


class Attendance(models.Model):
    SID = models.CharField(max_length=20)
    date = models.DateField()
    SW = models.TimeField()
    SG = models.TimeField()
    SL = models.BooleanField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

