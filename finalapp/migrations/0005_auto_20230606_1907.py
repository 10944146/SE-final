from django.db import migrations

def create_default_data(apps, schema_editor):
    Customer = apps.get_model('finalapp', 'customer')
    purchase = apps.get_model('finalapp', 'purchase')
    sales_details = apps.get_model('finalapp', 'SalesDetail')
    MassageChair = apps.get_model('finalapp', 'MassageChair')
    Branch = apps.get_model('finalapp', 'Branch')
    KPI = apps.get_model('finalapp', 'KPI')
    Salesperson = apps.get_model('finalapp', 'Salesperson')
    SalesTarget = apps.get_model('finalapp', 'SalesTarget')
    Coupon = apps.get_model('finalapp', 'Coupon')
    Attendance = apps.get_model('finalapp', 'Attendance')
    CouponUsage = apps.get_model('finalapp', 'CouponUsage')

    # Create default customers
    Customer.objects.create(CID='C211', CName='王小雪', CEmail='customer1@example.com', CStage='潛在客戶', CActrecord='2023/06/05試坐按摩椅並加入APP', CStartdate='2023-06-05', CDealdate=None, SID='S001', CDemand_description='腿部', CSpecial_requests='無', CAge_range='21-30', COccupation_category='運動員')
    Customer.objects.create(CID='C178', CName='陳小雯', CEmail='customer2@example.com', CStage='準客戶', CActrecord='2023/06/05試坐按摩椅並到店詢問', CStartdate='2023-06-05', CDealdate=None, SID='S002', CDemand_description='腰部', CSpecial_requests='無', CAge_range='31-40', COccupation_category='銀行員')
    Customer.objects.create(CID='C298', CName='王小菲', CEmail='customer3@example.com', CStage='結案', CActrecord='2023/06/05下訂單', CStartdate='2023-06-01', CDealdate='2023-06-05', SID='S003', CDemand_description='肩頸', CSpecial_requests='無', CAge_range='41-50', COccupation_category='工程師')
    Customer.objects.create(CID='C147', CName='陳小明', CEmail='customer4@example.com', CStage='潛在客戶', CActrecord='2023/06/05試坐按摩椅並加入APP', CStartdate='2023-06-05', CDealdate=None, SID='S004', CDemand_description='全身', CSpecial_requests='無', CAge_range='51-60', COccupation_category='農夫')
    Customer.objects.create(CID='C058', CName='陳曉晰', CEmail='customer5@example.com', CStage='準客戶', CActrecord='2023/06/05試坐按摩椅並到店詢問', CStartdate='2023-06-03', CDealdate=None, SID='S005', CDemand_description='腿部', CSpecial_requests='無', CAge_range='60以上', COccupation_category='廚師')
    Customer.objects.create(CID='C159', CName='汪曉婷', CEmail='customer15@example.com', CStage='潛在客戶', CActrecord='2023/06/08試坐按摩椅並加入APP', CStartdate='2023-06-08', CDealdate=None, SID='S006', CDemand_description='腿部', CSpecial_requests='', CAge_range='21-30', COccupation_category='護理師')
    Customer.objects.create(CID='C011', CName='王曉明', CEmail='customer2@example.com', CStage='準客戶', CActrecord='2023/06/05試坐按摩椅並到店詢問', CStartdate='2023-06-06', CDealdate=None, SID='S007', CDemand_description='腰部', CSpecial_requests='', CAge_range='31-40', COccupation_category='演員')
    Customer.objects.create(CID='C089', CName='陳小心', CEmail='customer3@example.com', CStage='結案', CActrecord='2023/06/05下訂單', CStartdate='2023-06-07', CDealdate='2023-06-05', SID='S008', CDemand_description='肩頸', CSpecial_requests='', CAge_range='41-50', COccupation_category='作家')
    Customer.objects.create(CID='C247', CName='陳雨鑫', CEmail='customer4@example.com', CStage='潛在客戶', CActrecord='2023/06/05試坐按摩椅並加入APP', CStartdate='2023-06-08', CDealdate=None, SID='S009', CDemand_description='全身', CSpecial_requests='', CAge_range='51-60', COccupation_category='工程師')
    Customer.objects.create(CID='C356', CName='劉小飛', CEmail='customer5@example.com', CStage='準客戶', CActrecord='2023/06/05試坐按摩椅並到店詢問', CStartdate='2023-06-09', CDealdate=None, SID='S010', CDemand_description='腿部', CSpecial_requests='', CAge_range='60以上', COccupation_category='教師')
    Customer.objects.create(CID='C123', CName='黃曉瑜', CEmail='customer6@example.com', CStage='潛在客戶', CActrecord='2023/06/08試坐按摩椅並加入APP', CStartdate='2023-06-08', CDealdate=None, SID='S011', CDemand_description='腰部', CSpecial_requests='', CAge_range='31-40', COccupation_category='教師')
    Customer.objects.create(CID='C231', CName='黃仔魚', CEmail='customer7@example.com', CStage='準客戶', CActrecord='2023/06/05試坐按摩椅並到店詢問', CStartdate='2023-06-11', CDealdate=None, SID='S012', CDemand_description='肩頸', CSpecial_requests='', CAge_range='41-50', COccupation_category='設計師')
    Customer.objects.create(CID='C221', CName='王愉馨', CEmail='customer8@example.com', CStage='結案', CActrecord='2023/06/05下訂單', CStartdate='2023-06-12', CDealdate='2023-06-05', SID='S013', CDemand_description='全身', CSpecial_requests='', CAge_range='51-60', COccupation_category='律師')
    Customer.objects.create(CID='C105', CName='劉小菁', CEmail='customer9@example.com', CStage='潛在客戶', CActrecord='2023/06/13試坐按摩椅並加入APP', CStartdate='2023-06-13', CDealdate=None, SID='S014', CDemand_description='腿部', CSpecial_requests='', CAge_range='21-30', COccupation_category='工程師')
    Customer.objects.create(CID='C154', CName='李小龍', CEmail='customer10@example.com', CStage='準客戶', CActrecord='2023/06/05試坐按摩椅並到店詢問', CStartdate='2023-06-14', CDealdate=None, SID='S015', CDemand_description='腰部', CSpecial_requests='', CAge_range='31-40', COccupation_category='工程師')
    Customer.objects.create(CID='C177', CName='李大程', CEmail='customer11@example.com', CStage='結案', CActrecord='2023/06/05下訂單', CStartdate='2023-06-15', CDealdate='2023-06-05', SID='S001', CDemand_description='肩頸', CSpecial_requests='', CAge_range='41-50', COccupation_category='銀行員')
    Customer.objects.create(CID='C206', CName='李曉菁', CEmail='customer12@example.com', CStage='潛在客戶', CActrecord='2023/06/16試坐按摩椅並加入APP', CStartdate='2023-06-16', CDealdate=None, SID='S015', CDemand_description='全身', CSpecial_requests='', CAge_range='51-60', COccupation_category='運動員')
    Customer.objects.create(CID='C136', CName='陳依昱', CEmail='customer13@example.com', CStage='準客戶', CActrecord='2023/06/05試坐按摩椅並到店詢問', CStartdate='2023-06-17', CDealdate=None, SID='S013', CDemand_description='腿部', CSpecial_requests='', CAge_range='60以上', COccupation_category='護理師')   
    
    # Create default purchases
    purchase.objects.create(PID='P001', BID='B001', MID='M001', PCost='8000',PAmount='100')
    purchase.objects.create(PID='P002', BID='B005', MID='M003', PCost='7000',PAmount='200')
    purchase.objects.create(PID='P003', BID='B002', MID='M005', PCost='7500',PAmount='200')
    purchase.objects.create(PID='P004', BID='B005', MID='M004', PCost='6000',PAmount='80')
    purchase.objects.create(PID='P005', BID='B004', MID='M002', PCost='10000',PAmount='120')
    purchase.objects.create(PID='P002', BID='B005', MID='M003', PCost='7000',PAmount='200')
    purchase.objects.create(PID='P003', BID='B002', MID='M005', PCost='7500',PAmount='150')
    purchase.objects.create(PID='P004', BID='B001', MID='M004', PCost='6000',PAmount='200')
    purchase.objects.create(PID='P002', BID='B002', MID='M003', PCost='7000',PAmount='100')
    purchase.objects.create(PID='P003', BID='B003', MID='M005', PCost='7500',PAmount='80')
    purchase.objects.create(PID='P005', BID='B004', MID='M002', PCost='10000',PAmount='70')
    purchase.objects.create(PID='P003', BID='B005', MID='M005', PCost='7500',PAmount='85')
    purchase.objects.create(PID='P002', BID='B001', MID='M003', PCost='7000',PAmount='90')
    purchase.objects.create(PID='P004', BID='B002', MID='M004', PCost='6000',PAmount='100')
    purchase.objects.create(PID='P002', BID='B001', MID='M003', PCost='7000',PAmount='250')
    purchase.objects.create(PID='P003', BID='B003', MID='M005', PCost='7500',PAmount='125')
    purchase.objects.create(PID='P005', BID='B003', MID='M002', PCost='10000',PAmount='110')
    purchase.objects.create(PID='P001', BID='B004', MID='M001', PCost='8000',PAmount='65')

    # Create default sales_details
    sales_details.objects.create(BID='B001', SID='S001',CID='C211',MID='M001',SAmount='1',SPrice='10000',SDiscount='0',SPay='10000',SDate='2023-06-05',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B002', SID='S002',CID='C178',MID='M001',SAmount='1',SPrice='10000',SDiscount='0',SPay='10000',SDate='2023-06-08',SRepurchase='0',SPayment='現金')
    sales_details.objects.create(BID='B003', SID='S003',CID='C298',MID='M002',SAmount='1',SPrice='20000',SDiscount='0',SPay='20000',SDate='2023-06-01',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B004', SID='S004',CID='C147',MID='M002',SAmount='1',SPrice='20000',SDiscount='0',SPay='20000',SDate='2023-06-05',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B005', SID='S005',CID='C058',MID='M003',SAmount='1',SPrice='14000',SDiscount='0',SPay='14000',SDate='2023-06-02',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B001', SID='S006',CID='C159',MID='M003',SAmount='1',SPrice='14000',SDiscount='0',SPay='14000',SDate='2023-06-05',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B002', SID='S007',CID='C011',MID='M004',SAmount='1',SPrice='12000',SDiscount='0',SPay='12000',SDate='2023-06-05',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B003', SID='S008',CID='C089',MID='M004',SAmount='1',SPrice='12000',SDiscount='0',SPay='12000',SDate='2023-06-04',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B004', SID='S009',CID='C247',MID='M005',SAmount='1',SPrice='15000',SDiscount='0',SPay='15000',SDate='2023-06-04',SRepurchase='0',SPayment='現金')
    sales_details.objects.create(BID='B005', SID='S010',CID='C356',MID='M005',SAmount='1',SPrice='15000',SDiscount='0',SPay='15000',SDate='2023-06-05',SRepurchase='0',SPayment='現金')
    sales_details.objects.create(BID='B001', SID='S011',CID='C123',MID='M001',SAmount='1',SPrice='10000',SDiscount='0',SPay='10000',SDate='2023-06-02',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B002', SID='S012',CID='C231',MID='M001',SAmount='1',SPrice='10000',SDiscount='0',SPay='10000',SDate='2023-06-03',SRepurchase='0',SPayment='現金')
    sales_details.objects.create(BID='B003', SID='S013',CID='C221',MID='M001',SAmount='1',SPrice='10000',SDiscount='0',SPay='10000',SDate='2023-05-30',SRepurchase='1',SPayment='信用卡')
    sales_details.objects.create(BID='B004', SID='S014',CID='C105',MID='M002',SAmount='1',SPrice='20000',SDiscount='0',SPay='20000',SDate='2023-05-31',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B005', SID='S015',CID='C154',MID='M002',SAmount='1',SPrice='20000',SDiscount='0',SPay='20000',SDate='2023-06-05',SRepurchase='0',SPayment='現金')
    sales_details.objects.create(BID='B001', SID='S015',CID='C177',MID='M002',SAmount='2',SPrice='20000',SDiscount='1600',SPay='20000',SDate='2023-05-31',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B005', SID='S013',CID='C206',MID='M005',SAmount='1',SPrice='15000',SDiscount='0',SPay='15000',SDate='2023-05-31',SRepurchase='0',SPayment='信用卡')
    sales_details.objects.create(BID='B004', SID='S001',CID='C136',MID='M005',SAmount='1',SPrice='15000',SDiscount='0',SPay='15000',SDate='2023-06-01',SRepurchase='0',SPayment='現金')
    sales_details.objects.create(BID='B003', SID='S010',CID='C206',MID='M005',SAmount='1',SPrice='15000',SDiscount='0',SPay='15000',SDate='2023-06-01',SRepurchase='0',SPayment='信用卡')


    # Create default MassageChair
    MassageChair.objects.create(MID='M001', MState='販售',PID='P001',BID='B001',MPrice='10000',MCost='8000',MAmount='0',MClass='實用按摩型')
    MassageChair.objects.create(MID='M002', MState='販售',PID='P002',BID='B002',MPrice='20000',MCost='10000',MAmount='0',MClass='高級豪華型')
    MassageChair.objects.create(MID='M003', MState='販售',PID='P003',BID='B003',MPrice='14000',MCost='7000',MAmount='0',MClass='經濟實惠型')
    MassageChair.objects.create(MID='M004', MState='販售',PID='P004',BID='B004',MPrice='12000',MCost='6000',MAmount='0',MClass='經濟實惠型')
    MassageChair.objects.create(MID='M005', MState='販售',PID='P005',BID='B005',MPrice='15000',MCost='75000',MAmount='0',MClass='實用按摩型')

    # Create default

    # Create default

    # Create default

    # Create default

    # Create default

    # Create default

    # Create default


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_data),
    ]
