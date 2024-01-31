from django.urls import path
from Userapp.views import SignUpView,SignInView,IndexView,sign_out_view
from django.contrib.auth import views as auth_views


urlpatterns=[

  path("register/",SignUpView.as_view(),name="signup"),
  path("login/",SignInView.as_view(),name="signin"),
  path("index/",IndexView.as_view(),name="index"),
  path('logout/',sign_out_view,name="signout"),
  path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),





]