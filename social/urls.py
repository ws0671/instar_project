from django.urls import path, include
from social import views

app_name = 'social'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('like/<int:article_pk>', views.like, name='like'),
    path('comment/<int:article_pk>', views.comment, name='comment'),
]
