from django.shortcuts import render
from .models import Salesperson



# Create your views here.
def sales_view(request):
    return render(request, 'sales.html')

def sales_view(request):
    salespersons = Salesperson.objects.all().order_by('SID')  
    context = {'salespersons': salespersons}
    return render(request, 'sales.html', context)

def salesindex_view(request):
    return render(request, 'salesindex.html')

def customer_view(request):
    return render(request, 'customer.html')
def customer1_view(request):
    return render(request, 'customer1.html')
def customer2_view(request):
    return render(request, 'customer2.html')
def customer3_view(request):
    return render(request, 'customer3.html')