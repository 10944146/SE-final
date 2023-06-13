from django.db import models

class customer(models.Model):
    CID = models.CharField(max_length=20, unique=True)
    CName = models.CharField(max_length=100)
    CStage = models.CharField(max_length=50)
    CAge_range = models.CharField(max_length=20)
    CGender = models.CharField(max_length=2,null=True)
    COccupation_category = models.CharField(max_length=50)
    CDemand_description = models.TextField(blank=True)
    CHow = models.CharField(max_length=20,null=True)
    BID = models.CharField(max_length=20,null=True)
    CMON = models.CharField(max_length=20,null=True)

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class purchase(models.Model):
    MID = models.CharField(max_length=20)
    MNAME = models.CharField(max_length=100,null=True)
    PCost = models.DecimalField(max_digits=10, decimal_places=2)
    PDate = models.DateField(null=True)
    MFuction= models.CharField(max_length=100,null=True)
    PAmount = models.IntegerField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class SalesDetail(models.Model):
    CID = models.CharField(max_length=20)
    MID = models.CharField(max_length=20)
    MNAME = models.CharField(max_length=100,null=True)
    CAge_range = models.CharField(max_length=20,null=True)
    SAmount = models.IntegerField()
    SPrice = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class MassageChair(models.Model):
    MID = models.CharField(max_length=20)
    MNAME = models.CharField(max_length=100,null=True)
    MCost = models.DecimalField(max_digits=10, decimal_places=2)
    MPrice = models.DecimalField(max_digits=10, decimal_places=2)
    MState = models.BooleanField()
    MFuction= models.CharField(max_length=100,null=True)
    MAmount = models.IntegerField()

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳

class EXM(models.Model):
    MID = models.CharField(max_length=20)
    MNAME = models.CharField(max_length=100,null=True)
    MFuction= models.CharField(max_length=100,null=True)
    EXMAmount = models.IntegerField(null=True)

    # def __str__(self):
        #return self.customer_name
    #讓object預設回傳
    

class Branch(models.Model):
    BID = models.CharField(max_length=20)
    BName=models.CharField(max_length=20,null=True)
    SID = models.CharField(max_length=20)
    SMON = models.CharField(max_length=20,null=True)
    SAc = models.IntegerField(null=True)
    STc = models.IntegerField(null=True)
    SNew = models.IntegerField(null=True)
    SOld = models.IntegerField(null=True)
    SOSALE = models.IntegerField(null=True)
    SNSALE = models.IntegerField(null=True)


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
    SName=models.CharField(max_length=20,null=True)
    SQ = models.IntegerField()
    SR = models.IntegerField()
    STQ = models.IntegerField()
    SM1= models.IntegerField(null=True)
    SM2= models.IntegerField(null=True)
    SM3= models.IntegerField(null=True)
    SARR= models.IntegerField(null=True)
    SLE= models.IntegerField(null=True)

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

