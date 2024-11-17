"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from tasks.views import add_task_view,delete_task_view,GenericTaskView,GenericTaskCreateView,UserCreateView,UserLoginView, GenericTaskUpdateView,GenericTaskDetailView,GenericTaskDeleteView,session_storage_view
from tasks.apiviews import TaskListAPI
from rest_framework.routers import SimpleRouter
from tasks.apiviews import TaskViewSet
from django.contrib.auth.views import LogoutView

router = SimpleRouter()

router.register('api/task',TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('taskapi',TaskListAPI.as_view()),
    path('task',GenericTaskView.as_view()),
    path('create-task',GenericTaskCreateView.as_view()),
    path('update-task/<pk>',GenericTaskUpdateView.as_view()),
    path('detail-task/<pk>',GenericTaskDetailView.as_view()),
    path('delete-task/<pk>',GenericTaskDeleteView.as_view()),
    path('user/login',UserLoginView.as_view()),
    path('user/logout',LogoutView.as_view()),
    path('sessiontest',session_storage_view),
    path('user/signup',UserCreateView.as_view()),
    path('add-task',add_task_view),
    # path("delete-task/<int:index>",delete_task_view),
    # path('add-comp-task',add_com_task_view),
    # path("delete-comp-task/<int:val>",delete_comp_task_view),
] + router.urls
