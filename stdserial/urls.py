
from django.contrib import admin
from django.urls import path,include
from stdserial import views
urlpatterns = [

    path('stdinfo/<int:pk>',views.student_details,name='student_info'),
    path('stdinfo/',views.student_list,name='student_list')
]
