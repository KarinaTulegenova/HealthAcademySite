from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('service/<int:service_id>/', views.service_detail_view, name='service_detail'),
    path('book-appointment/<int:service_id>/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('checkout/<str:billing_id>/', views.checkout_view, name='checkout'),
    path('stripe-payment/<str:billing_id>/', views.stripe_payment, name='stripe_payment'),
    path('stripe-payment-verify/<str:billing_id>/', views.stripe_payment_verify, name='stripe_payment_verify'),
    path('payment-status/<str:billing_id>/', views.payment_status_view, name='payment_status'),
]