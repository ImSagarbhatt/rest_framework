from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentList.as_view()),
    path('student/<int:pk>', views.StudentDetail.as_view()),

]
