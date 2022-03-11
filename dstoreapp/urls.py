from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexa,name='indexa'),
    path('about1',views.about1,name='about1'),
    path('contact1',views.contact1,name='contact1'),
    path('register1',views.register1,name='register1'),
    path('getstore',views.getstore,name='getstore'),
    path('regi1',views.regi1,name='regi1'),
    path('registration',views.registration,name='registration'),
    path('userlogin1',views.userlogin1,name='userlogin1'),
    path('userin1',views.userin1,name='userin1'),
    path('logout1',views.logout1,name='logout1'),
    path('contacttable',views.contacttable,name='contacttable'),
    path('products',views.products,name='products'),
    path('single/<int:pid>',views.single,name='single'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('cart1/<int:pid>/',views.cart1,name='cart1'),
    path('deletec/<int:cid>/',views.deletec,name='deletec'),
    path('checkout1',views.checkout1,name='checkout1'),
    path('cart_update',views.cart_update,name='cart_update'),
    path('orders',views.orders,name='orders'),
    path('getorder',views.getorder,name='getorder')
   
]