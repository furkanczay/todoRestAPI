from django.urls import path, include
from . import views

urlpatterns = [
    path('todos/', include([
        path('', views.TodoListApiView.as_view(), name='todo_list'),
        path('<int:pk>/', views.TodoDetailApiView.as_view(), name='todo_detail'),
        path('create/', views.TodoCreateApiView.as_view(), name='todo_create'),
        path('update/<int:pk>/', views.TodoUpdateApiView.as_view(), name='todo_update'),
        path('delete/<int:pk>/', views.TodoDestroyApiView.as_view(), name='todo_delete'),
    ]))
]