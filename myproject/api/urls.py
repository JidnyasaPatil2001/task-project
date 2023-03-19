from django.urls import path
from . import views


urlpatterns=[
    path('',views.getallclient),
    path('add/',views.addclient),
    path('display/<int:pk>/',views.getclient),
    path('update/<int:pk>/',views.updateclient),
    path('delete/<int:pk>/',views.deleteclient),
    # path('login/', views.LoginView.as_view()),
    # path('users/',views.Userlist),
    # path('addusers/',views.addUser)

]
