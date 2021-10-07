from django.urls import path
from .views import *
from .views_uy import Search_products,Instruction

app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('cat/', cat, name='cat'),
    path('instruction/', Instruction.as_view(), name='instruction'),
    path('sign-up/',login, name='sign-up'),
    path('login/', UserD.as_view(), name='login'),
    path('registration/', RegistrationUser.as_view(), name='registration'),
    path('logout/', RegistrationUser.as_view(), name='logout'),
    path('instruction/', RegistrationUser.as_view(), name='instruction'),
    path('Logout/', logouts, name="logout"),
    path('myaccount/', MyAccount.as_view(), name='myaccount'),
    path('tuman/<int:pk>/',Uy_index.as_view(), name='index'),
    path('detail/<int:pk>', detail, name='detail'),
    path('uydelete/<int:pk>', uydelete, name='uydelete'),
    path('search_products', Search_products, name='search_products'),

]