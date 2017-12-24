from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog_index'),
    path('/view/(?P<pk>\d+)',views.view_post, name='view_post'),
    path('/delete/(?P<pk>\d+)', views.entry_delete, name='entry_delete'),
    path('category/(?P<pk>\d]+)',views.view_category, name='view_category'),
    path('/edit/(?P<pk>\d+)', views.entry_update,name='entry_update'),
    #path('/edit/(?P<pk>\d+)', views.UpdateEntry.as_view(), name='entry_update'),
    path('search/', views.search, name='search'),
    path('add/', views.add_entry, name='add_entry'),
    path('resume/', views.display_resume, name='resume'),
    #path('add/', views.AddEntry.as_view(), name='add_entry'),
]