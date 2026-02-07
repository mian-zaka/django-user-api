from django.urls import path
from .import views
urlpatterns = [
    path('list-users/',views.list_users),
    path('user/<int:id>',views.get_user),
    path('userDelete/<int:id>',views.deleteUser),
    path('userUpdate/<int:id>',views.updateUser),
    path('createUser',views.CreateUser)]