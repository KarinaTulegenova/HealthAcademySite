from django.urls import path
from . import views

app_name = 'physician'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointment/<str:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('appointment/<str:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),
    path('appointment/<str:appointment_id>/complete/', views.complete_appointment, name='complete_appointment'),
    path('appointment/<str:appointment_id>/activate/', views.activate_appointment, name='activate_appointment'),
    path('appointment/<str:appointment_id>/add-medical-record/', views.add_medical_record, name='add_medical_record'),
    path('appointment/<str:appointment_id>/medical-record/<int:medical_record_id>/edit/', views.edit_medical_record, name='edit_medical_record'),
    path('appointment/<str:appointment_id>/add-lab-test/', views.add_lab_test, name='add_lab_test'),
    path('appointment/<str:appointment_id>/lab-test/<int:lab_test_id>/edit/', views.edit_lab_test, name='edit_lab_test'),
    path('appointment/<str:appointment_id>/add-prescription/', views.add_prescription, name='add_prescription'),
    path('appointment/<str:appointment_id>/prescription/<int:prescription_id>/edit/', views.edit_prescription, name='edit_prescription'),
    path('payments/', views.payments, name='payments'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/<int:id>/mark-as-read/', views.mark_as_read_notifications, name='mark_as_read_notifications'),
    path('profile/', views.profile, name='profile'),
]