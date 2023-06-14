from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('', views.company, name='company'), 
    path('customer/', views.customer_view, name='customer'),
    path('customer1/', views.customer1_view, name='customer1'),
    path('customer2/', views.customer2_view, name='customer2'),
    # path('customer3/', views.customer3_view, name='customer3.html'),
    path('salesindex/', views.salesindex_view, name='salesindex.html'),
    path('salesindex/', views.salesindex, name='salesindex.html'),
    path('salesindex/sales.html', views.sales, name='sales'),
    path('salesindex/', views.salesindex_view, name='salesindex'),
    path('get-salesperson-data', views.get_salesperson_data, name='get_salesperson_data'),
    path('branch/', views.branch, name='branch.html'),
    path('branch/', views.branch_view, name='branch'),
    path('branch/<str:branch>/', views.branch_view, name='branch'),
    path('chair/', views.chair, name='chair'),
]