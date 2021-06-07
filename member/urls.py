from django.urls import path
from member import views

app_name = 'member'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('main/', views.main, name='main'),

    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit'),
]