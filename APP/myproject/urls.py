"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name = 'welcome'),
    path('signin', views.Sign_in, name ='signin'),
    path('logout', views.sign_out, name = 'logout'),
    path('register', views.SignUP, name = 'signup'),
    path('profile', views.profile, name = 'profile'),
    path('todo_list', views.todo_list, name = 'todo_list'),
    path('todo_detail/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('add_todo', views.add_todo, name='add_todo'), 
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),  
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('add_subtask/<int:todo_id>/', views.add_subtask, name='add_subtask'),  
    path('edit_subtask/<int:subtask_id>/', views.edit_subtask, name='edit_subtask'),  
    path('delete_subtask/<int:subtask_id>/', views.delete_subtask, name='delete_subtask'),  
    path('update_todo/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('update_subtask/<int:subtask_id>/', views.update_subtask, name='update_subtask'),

    path('update/<int:todo_id>/', views.update_todo, name='update_todo'),
]

