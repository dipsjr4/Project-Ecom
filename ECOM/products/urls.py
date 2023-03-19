from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('pages/<int:pk>/', views.detail, name='detail'),
]
