from django.urls import path
from business import views

urlpatterns = [
    path('', views.show_business, name='home'),
    path('Register', views.showRegister, name='Register'),
    path('login', views.showlogin, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('service', views.port, name='portfolio'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('Job-apply', views.jobapply, name='Jobapply')
]
