from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('add_category',views.add_category,name='add_category'),
    path('view_category',views.view_category,name='view_category'),
    path('getdata',views.getdata,name='getdata'),
    path('edit/<int:trid>/',views.edit,name='edit'),
    path('update/<int:uid>/',views.update,name='update'),
    path('delete/<int:did>/)',views.delete,name='delete'),
    path('add_product',views.add_product,name='add_product'),
    path('view_product',views.view_product,name='view_product'),
    path('getpro',views.getpro,name='getpro'),
    path('edit1/<int:eid>/',views.edit1,name='edit1'),
    path('update1/<int:pid>/',views.update1,name='update1'),
    path('delete1/<int:lid>/)',views.delete1,name='delete1'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adlogin',views.adlogin,name='adlogin')
]