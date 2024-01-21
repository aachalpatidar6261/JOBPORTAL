from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),

    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('job_list/', views.job_list, name='job_list'),
    path('category/', views.category, name='category'),
    path('apply/', views.apply, name='apply'),


    path('company_index/',views.company_index , name='company_index'),
    path('company_add_jobs/', views.company_add_jobs, name='company_add_jobs'),
    path('company_about/', views.company_about, name='company_about'),

    

    




]
