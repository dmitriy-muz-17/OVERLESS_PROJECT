from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 #path('login/', views.user_login, name='login'), моя реализация аунтификаци ( основной минус плохая оптимизация)
 path('login/', auth_views.LoginView.as_view(), name='login'),
 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 path('', views.dashboard, name='dashboard'),
 path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
 path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
 path('edit/', views.edit, name='edit'),
 path('users/', views.user_list, name='user_list'),
 path('users/follow/', views.user_follow, name='user_follow'),
 path('users/<username>/', views.user_detail, name='user_detail'),
 path('register/', views.register, name='register'),
 ]
