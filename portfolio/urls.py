from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pdf/', views.gen_pdf, name ="pdf"),
]