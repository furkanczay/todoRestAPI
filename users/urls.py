from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', include([
        path('', views.UserListApiView.as_view(), name='user_list'),
        path('<int:pk>/', views.UserDetailApiView.as_view(), name='user_detail'),
    ])),
    path('groups', include([
        path('', views.GroupListApiView.as_view(), name='group_list'),
    ]))
]