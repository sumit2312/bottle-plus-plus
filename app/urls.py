

from django.urls import path, re_path
from app import views


urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('patients/', views.get_patients_list, name="get_patients_list"),
    # path('<int:pk>/', views.PatientDetailView.as_view(), name='detail'),
    path('patients/<int:pk>', views.get_patient_info, name="get_patient_info"),
    path('notifications/', views.notifications, name="notifications"),
]
