from django.urls import path, include
from social import views

app_name = 'social'

urlpatterns = [
    path('upload/', views.upload, name='upload'),

]
