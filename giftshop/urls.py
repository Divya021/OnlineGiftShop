"""onlinebookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('send_feedback/(?P<pid>[0-9]+)', Feedback, name='send_feedback'),
    path('delete_feedback/(?P<pid>[0-9]+)', Delete_feedback, name='delete_feedback'),
    path('contact/',Contact,name='contact'),
    path('feedback/',Feedback,name='view_feedback'),
    path('login/',Login,name='login'),
    path('profile', Add_Profile, name='profile'),
    path('login_admin', Login_Admin, name='login_admin'),
    path('admin_base', Admin_Base, name='admin_base'),
    path('view_product/', View_Product, name='view_product'),
    path('view_categary/', View_Categary, name='view_categary'),
    path('admin_view_product/', Admin_View_Product, name='admin_view_product'),
    path('basekin/(?P<pid>[0-9]+)', Product_booking, name='basekin'),
    path('add_product', Add_Product, name='add_product'),
    path('add_categary', Add_Categary, name='add_categary'),
    path('view_feedback', View_feedback, name='view_feedback'),
    path('view_customer', View_Customer, name='view_customer'),
    path('admin_viewBooking', Admin_View_Booking, name='admin_viewBooking'),
    path('logout_admin', Logout_Admin, name='logout_admin'),
    path('logout/',Logout,name='logout'),
    path('change_password/',change_password,name='change_password'),
    path('admin_profile/(?P<pid>[0-9]+)', Admin_Profile, name='admin_profile'),
    path('edit_product/(?P<pid>[0-9]+)',Edit_Product, name='edit_product'),
    path('delete_product/(?P<pid>[0-9]+)',delete_product, name='delete_product'),
    path('delete_categery/(?P<pid>[0-9]+)',delete_categary, name='delete_categary'),
    path('delete_customer/(?P<pid>[0-9]+)',Delete_Customer, name='delete_customer'),
    path('booking/(?P<pid>[0-9]+)',Booking_order, name='booking'),
    path('delete_booking/(?P<pid>[0-9]+)', delete_booking, name='delete_booking'),
    path('payment1/(?P<pid>[0-9]+)', Payment1, name='payment1'),
    path('payment2', Payment, name='payment2'),
    path('view_profile',View_profile, name='view_prifile'),
    path('view_booking', View_Booking, name='view_booking'),
     path('edit_profile/(?P<pid>[0-9]+)', Edit_Profile, name='edit_profile'),
    path('status/(?P<pid>[0-9]+)', Edit_status, name='status'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
