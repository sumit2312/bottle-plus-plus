from django.urls import path
from . import views

urlpatterns = [
    path('get_patients_list/', views.get_patients_list),
    path("get_bottle_info/<int:pk>", views.get_bottle_info),
    #path('patients/<int:pk>/', views.get_patients_detail),
    path('update_bottle_level/<int:pk>', views.update_bottle_level),
    
]