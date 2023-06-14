from django.shortcuts import render
from .models import Salesperson, Branch, profit, customer
from django.template.defaultfilters import floatformat
from django.db.models import Sum, Count
from django.http import JsonResponse


# Create your views here.
def company(request):
    totalthisJuly = Branch.objects.filter(SMON=6).aggregate(totalthisJuly=Sum('SNSALE'))['totalthisJuly']
    totalpastJuly = Branch.objects.filter(SMON=6).aggregate(totalpastJuly=Sum('SOSALE'))['totalpastJuly']
    totalthisMay = Branch.objects.filter(SMON=5).aggregate(totalthisMay=Sum('SNSALE'))['totalthisMay']
    totalpastMay = Branch.objects.filter(SMON=5).aggregate(totalpastMay=Sum('SOSALE'))['totalpastMay']
    totalthisApril = Branch.objects.filter(SMON=4).aggregate(totalthisApril=Sum('SNSALE'))['totalthisApril']
    totalpastApril = Branch.objects.filter(SMON=4).aggregate(totalpastApril=Sum('SOSALE'))['totalpastApril']
    totalthisMarch = Branch.objects.filter(SMON=3).aggregate(totalthisMarch=Sum('SNSALE'))['totalthisMarch']
    totalpastMarch = Branch.objects.filter(SMON=3).aggregate(totalpastMarch=Sum('SOSALE'))['totalpastMarch']
    return render(request, 'company.html', {
            'totalthisJuly': totalthisJuly,
            'totalpastJuly': totalpastJuly,
            'totalthisMay': totalthisMay,
            'totalpastMay': totalpastMay,
            'totalthisApril': totalthisApril,
            'totalpastApril': totalpastApril,
            'totalthisMarch': totalthisMarch,
            'totalpastMarch': totalpastMarch,
        }
    )

def sales(request):
    salesperson = request.GET.get('salesperson')
    # 根据销售人员参数从数据库中获取相应的数据
    salesperson_data = Salesperson.objects.get(SName=salesperson)
    
    return render(request, 'sales.html', {'salesperson': salesperson_data})

# def sales_view(request):
#     salespersons = Salesperson.objects.all().order_by('SID')  
#     context = {'salespersons': salespersons}
#     return render(request, 'sales.html', context)

def salesindex_view(request):
    salespersons = Salesperson.objects.all().order_by('SID')  
    context = {'salespersons': salespersons}
    return render(request, 'salesindex.html', context)

def salesindex(request):
    return render(request, 'salesindex.html')

# 先寫死成6月跟中壢中原店 # 後續可根據進入的分店頁面決定BID
def customer_view(request):
    Newcustomer = customer.objects.filter(CMON="6", BID="B001").count()
    Perfer = customer.objects.filter(BID="B001").values('CDemand_description').annotate(count=Count('CDemand_description')).order_by('-count')[0]['CDemand_description']
    Recommend = customer.objects.filter(BID="B001").values('CHow').annotate(count=Count('CHow')).order_by('-count')[0]['CHow']
    age1 = customer.objects.filter(CAge_range="20-29", BID="B001").count()
    age2 = customer.objects.filter(CAge_range="30-39", BID="B001").count()
    age3 = customer.objects.filter(CAge_range="40-49", BID="B001").count()
    age4 = customer.objects.filter(CAge_range="50-59", BID="B001").count()
    age5 = customer.objects.filter(CAge_range="60以上", BID="B001").count()
    sum = age1 + age2 + age3 + age4 + age5
    return render(
        request, 
        'customer.html', {
            'Newcustomer': Newcustomer, 
            'Perfer': Perfer, 
            'Recommend': Recommend,
            'age1': age1,
            'age2': age2,
            'age3': age3,
            'age4': age4,
            'age5': age5,
            'sum': sum,
        }
    )

def customer1_view(request):
    return render(request, 'customer1.html')
def customer2_view(request):
    return render(request, 'customer2.html')
def customer3_view(request):
    return render(request, 'customer3.html')

def get_salesperson_data(request):
    salesperson_name = request.GET.get('salesperson')
    salesperson = Salesperson.objects.get(SName=salesperson_name)

    max_value = max(salesperson.SM1, salesperson.SM2, salesperson.SM3)

    if max_value == salesperson.SM1:
        max_name = "經濟實惠型"
    elif max_value == salesperson.SM2:
        max_name = "實用按摩型"
    elif max_value == salesperson.SM3:
        max_name = "高級豪華型"
    else:
        max_name = ""

    achievement_rate = (salesperson.SQ / salesperson.STQ) * 100

    data = {
        'SR': str(salesperson.SR),
        'SQ': str(salesperson.SQ),
        'achievement_rate': format(achievement_rate, '.2f'),
        'max_name': max_name,
        'SARR': str(salesperson.SARR),
        'SLE': str(salesperson.SLE),
        'SM1': str(salesperson.SM1),
        'SM2': str(salesperson.SM2),
        'SM3': str(salesperson.SM3)
    }
    return JsonResponse(data)

def branch(request):
    return render(request, 'branch.html')



def branch_view(request, branch):
    name_mapping = {
        'S001': '潘於新',
        'S002': '江姜好',
        'S003': '邱汪明',
        'S004': '邱曉愈',
        'S005': '劉心瑀',
        'S006': '劉心成',
        'S007': '李冠郁',
        'S008': '黃盛餘',
        'S009': '黃新衣',
        'S010': '陳大賀',
        'S011': '汪曉明',
        'S012': '陳一新',
    }

    branches = list(Branch.objects.filter(BID=branch, SMON='5').order_by('SID'))
    
    sids = []
    sacs = []
    snsales = []
    for branch_obj in branches:
        sid = branch_obj.SID
        sids.append(sid)
        sacs.append(branch_obj.SAc)
        snsales.append(branch_obj.SNSALE)
    
    names = [name_mapping.get(sid, '') for sid in sids]
    
    if branch_obj:
        branch_name = branch_obj.BName
    else:
        branch_name = ""
        
    sac_sum = sum(sacs)
    stc_sum = Branch.objects.filter(BID=branch, SMON='5').aggregate(stc_sum=Sum('STc'))['stc_sum']

    if stc_sum is None:
        return render(request, 'branch.html', {'branch_code': branch})

    achieved_percent = int((sac_sum / stc_sum) * 100)
    not_achieved_percent = 100 - achieved_percent

    new_sum = 0
    old_sum = 0
    branch_obj = Branch.objects.filter(BID=branch).first()
    if branch_obj:
        new_sum = branch_obj.SNew
        old_sum = branch_obj.SOld
    data3 = list(profit.objects.filter(BID=branch, year=2022).values_list('one', 'two', 'three', 'four', 'five', 'six').first())
    data4 = list(profit.objects.filter(BID=branch, year=2023).values_list('one', 'two', 'three', 'four', 'five', 'six').first())

    diff_6 = data4[5] - data3[5] + 12
    diff_5 = data4[4] - data3[4]
    diff_4 = data4[3] - data3[3]
    diff_3 = data4[2] - data3[2]
    diff_2 = data4[1] - data3[1]

    context = {
        'branch_code': branch,
        'names': names,
        'branch_name': branch_name,
        'sacs': sacs,
        'achieved_percent': achieved_percent,
        'not_achieved_percent': not_achieved_percent,
        'new_percent': new_sum / (new_sum + old_sum),
        'old_percent': old_sum / (new_sum + old_sum),
        'data3': data3,
        'data4': data4,
        'diff_6': diff_6,
        'diff_5': diff_5,
        'diff_4': diff_4,
        'diff_3': diff_3,
        'diff_2': diff_2,
        'sids_array': sids,
        'snsales_array': snsales,
    }

    return render(request, 'branch.html', context)

def chair(request):
    return render(request, 'chair.html')