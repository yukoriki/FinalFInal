from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='Login'),
    path('logout/', views.logout_user, name='Logout'),
    path('register/', views.register_user, name='Register'),
    path('record/<int:pk>', views.applicant_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]