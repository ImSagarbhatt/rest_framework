from django.urls import path
from . import views

urlpatterns = [
    path('', views.listview, name='alldata'),
    path('<int:pk>', views.detailview, name='oneobject'),
    path('create/', views.createview, name='create'),
    path('update/', views.updateview, name='update'),

]
