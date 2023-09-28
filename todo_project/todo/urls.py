from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('remove_task/<int:task_id>/', views.remove_task, name='remove_task')
]