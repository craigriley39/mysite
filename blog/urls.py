from django.urls import path
from . import views



app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog_index'),
    path('/view/(?P<slug>[\w-]+)',views.view_post, name='view_post'),
    path('category/(?P<slug>[\w-]+)',views.view_category, name='view_category'),

    path('search/', views.search, name='search'),
    path('add/', views.add_entry, name='add_entry')
]