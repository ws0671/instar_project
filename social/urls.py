from django.urls import path, include
from social import views

app_name = 'social'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('like/<int:article_pk>', views.like, name='like'),
    path('comment/<int:article_pk>', views.comment, name='comment'),
    path('tag/detail/<int:tag_pk>', views.tag_detail, name='tag-detail'),
]
