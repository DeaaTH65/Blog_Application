from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, CreateProfilePageView, EditProfilePageView
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password-success'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create-profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit-profile-page'),
]
