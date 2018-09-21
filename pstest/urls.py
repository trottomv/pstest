"""pstest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from oscar.app import application
from django.conf import settings
from oscarapi.app import application as api_product
import paypal.express.urls
from core import views as core_views
# from django.core.urlresolvers import reverse

from paypal.payflow.dashboard.app import application as payflow
from paypal.express.dashboard.app import application as express_dashboard
from django.conf.urls import url

from oscarapi import views as oscar_views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0
    path('admin/', admin.site.urls),
    path('', application.urls),  # > Django-2.0
    path('api/', api_product.urls),
    path('api/allproducts/', core_views.Products),
    path('api/hw/', core_views.HelloWorld),
    path('api-auth/', include('rest_framework.urls')),
    path('checkout/paypal/', include('paypal.express.urls')),
]
