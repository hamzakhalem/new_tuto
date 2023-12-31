from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name="index"),
    path('subscribe', views.subscribe , name="subscribe"),
    path('displayEmployee', views.displayEmployee , name="displayEmployee"),
    path('displayEmployee2', views.JasonClass.as_view(), name="displayEmployee2"),
    path('Employee/api/get/', views.EmployeeCv.as_view(), name="displayEmployee2"),
    path('create', views.RegistrationCreate.as_view() , name="createregistartion"),
    path('list', views.RegistrationList.as_view() , name="Listregistartion"),
    path('detail/<pk>', views.RegistrationDetail.as_view() , name="Detailregistartion"),
    path('update/<pk>', views.RegistrationUpdate.as_view() , name="Updateregistartion"),
    path('delete/<pk>', views.RegistrationDelete.as_view() , name="Deleteregistartion"),
]