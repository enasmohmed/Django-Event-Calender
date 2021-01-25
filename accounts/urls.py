from django.conf.urls import url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views
from .views import signup

app_name = 'accounts'

urlpatterns = [
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile_detail, name='profile_detail'),
    path('accounts/profile/edit/',views.profile_edit , name='profile_edit'),
    path('profile/change_password/',views.change_password , name='change_password'),
    path('accounts/activate/<uid>/<token>/', views.activate_email, name='activate_email'),


    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]