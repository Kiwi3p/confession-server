# quickstart/urls.py
# DataFlair
from django.urls import include, re_path as path
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views

urlpatterns = [
    path('api/', views.API_objects.as_view()),
    path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)