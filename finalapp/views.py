from django.shortcuts import render
from .models import Salesperson, Branch,SalesDetail
from django.http import JsonResponse



# Create your views here.

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

def customer_view(request):
    return render(request, 'customer.html')
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

def branch_view(request):
    return render(request, 'branch.html')
