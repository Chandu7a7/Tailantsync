from django.contrib import admin
from django.urls import path,include
from Home import views
from django.contrib.auth import views as auth_views
from . import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index , name="Home"),
    path("login/", views.signin , name="login"),
    path("signup/", views.signup , name="signup"),
    # path("contact/", views.contacts , name="contact"),
    path("logout/", views.logout_view , name="logout"),
    path("About/", views.About, name="About"),
    path("Assesment/", views.Assesment, name="Assesment"),
    path("Blog/", views.Blog, name="Blog"),
    path("Contact/", views.con, name="Contact"),
    path("Footer/", views.Footer, name="Footer"),
    path("Courses/", views.Courses, name="Courses"),
    path("Dashboard/", views.Dashboard, name="Dashboard"),
    path("Faq/", views.Faq, name="Faq"),
    path("Library/", views.Library, name="Library"),
    path("Navbar/", views.Navbar, name="Navbar"),
    path("Quizlanding/", views.Quizlanding, name="Quizlanding"),
    path("Quiz10/", views.Quiz10, name="Quiz10"),
    path("Innerlibrary/", views.Innerlibrary, name="Innerlibrary"),
    path("DashAbout/", views.DashAbout, name="DashAbout"),
    path('DashCourses/', views.DashCourses, name='DashCourses'),
    path('Dashteacher/', views.Dashteacher, name='Dashteacher'),
    path('DashContact/', views.DashContact, name='DashContact'),
    path('Dashplaylist/', views.Dashplaylist, name='Dashplaylist'),
    path('Dashviewprofile/', views.Dashviewprofile, name='Dashviewprofile'),
    path('Servicesinnerlibrary/', views.Servicesinnerlibrary, name='Servicesinnerlibrary'),
    path('Diffenceinnerlibrary/', views.Diffenceinnerlibrary, name='Diffenceinnerlibrary'),
    path('Designinnerlibrary/', views.Designinnerlibrary, name='Designinnerlibrary'),
    path('Engineeringinnerlibrary/', views.Engineeringinnerlibrary, name='Engineeringinnerlibrary'),
    path('Lawinnerlibrary/', views.Lawinnerlibrary, name='Lawinnerlibrary'),
    path('Marketinginnerlibrary/', views.Marketinginnerlibrary, name='Marketinginnerlibrary'),
    path('Box8th/', views.Box8th, name='Box8th'),
    path('Box9th/', views.Box9th, name='Box9th'),
    path('Box10th/', views.Box10th, name='Box10th'),
    path('Box11th/', views.Box11th, name='Box11th'),
    path('Box8th/', views.Box8th, name='Box8th'),
    path('Teacherprofile/', views.Teacherprofile, name='Teacherprofile'),
    path('DashteacherRegister/', views.DashteacherRegister, name='DashteacherRegister'),




    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    

  
]

    # path('reset_password/' , auth_views.PasswordResetView.as_view(template_name = "Home/templates/login.html") , name="reset_password"),