"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from ecom import settings
import app1.views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',app1.views.Login,name='login'),
    path('reg_form/',app1.views.reg_form_view,name='reg_form'),
    path('',app1.views.home,name='home'),
    path('adminhm/',app1.views.adminhm,name='adminhm'),
    path('index/',app1.views.index,name='index'),
    path('productadd/',app1.views.productadd,name='productadd'),
    path('userhm/',app1.views.userhm,name='userhm'),
    path('carts/<int:id>/', app1.views.carts, name='carts'),
    path('productdet/<int:id>/', app1.views.productdet, name='productdet'),
    path('listcart/',app1.views.listcart,name='listcart'),
    path('remove_from_cart/<int:item_id>/', app1.views.remove_from_cart, name='remove_from_cart'),
    path('orderview/',app1.views.orderview,name='orderview'),
    path('delete_order/<int:order_child_id>/',app1.views.delete_order,name='delete_order')
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
