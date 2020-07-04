from django.urls import path, include

from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_view, name='category_posts')
]
