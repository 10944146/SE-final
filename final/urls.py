"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finalapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('sales/', views.sales, name='sales.html'),
    path('customer/', views.customer_view, name='customer.html'),
    path('customer1/', views.customer1_view, name='customer1.html'),
    path('customer2/', views.customer2_view, name='customer2.html'),
    path('customer3/', views.customer3_view, name='customer3.html'),
    path('salesindex/', views.salesindex_view, name='salesindex.html'),
    path('salesindex/', views.salesindex, name='salesindex.html'),
    path('salesindex/sales.html', views.sales, name='sales'),
    path('salesindex/', views.salesindex_view, name='salesindex'),
    path('get-salesperson-data', views.get_salesperson_data, name='get_salesperson_data'),
]


