
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',Signup.as_view() , name="signup"),
    path('signin/', Singin.as_view(), name="signin"),
    path('logout/', logout_view, name="logout"),
    path('', home , name="home"),


    # registration urls
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    path('email_verify/<uuid:token>/', email_verify, name='email_verify'),
]
