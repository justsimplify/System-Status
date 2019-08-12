from django.urls import path

from . import views

urlpatterns = [
    path('getData/', views.get_data, name='get_data'),
    path('getData/<pk>/', views.get_data_by_key, name='get_data_by_key'),
    path('hook/', views.hook, name='hook'),
    path('produce_data/<pk>/', views.produce_data, name='produce_data'),
    path('view/', views.view, name='mainview'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
    path('<uri>/<timeout>/', views.index, name='index'),
]
