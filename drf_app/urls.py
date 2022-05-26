from django.urls import path
from . import views

urlpatterns = [
    path('', views.listview, name='alldata'),
    path('<int:pk>', views.detailview, name='oneobject'),

]
