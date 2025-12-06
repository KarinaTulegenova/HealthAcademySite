from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointment/<str:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('appointment/<str:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),
    path('appointment/<str:appointment_id>/complete/', views.complete_appointment, name='complete_appointment'),
    path('appointment/<str:appointment_id>/activate/', views.activate_appointment, name='activate_appointment'),
    path('payments/', views.payments, name='payments'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/<int:id>/mark-as-read/', views.mark_as_read_notifications, name='mark_as_read_notifications'),
    path('profile/', views.profile, name='profile'),
]