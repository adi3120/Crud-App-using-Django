from django.urls import path
from . import views

app_name = 'crudapp'
urlpatterns=[
	path('',views.list_view,name='index'),
	path('create',views.create_view,name='index'),
	path('list',views.list_view,name='list'),
	path('<int:data_id>/',views.detail_view,name='detail'),
	path('<int:data_id>/update',views.update_view,name='update'),
	path('<int:data_id>/delete',views.delete_view,name='delete'),
]