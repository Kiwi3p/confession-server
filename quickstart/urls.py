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
	# path('api/', views.Question_objects.as_view()),
	path('question-list/', views.questionList, name="question-list"),
	path('question-detail/<str:pk>/', views.questionDetail, name="question-detail"),
	path('question-create/', views.questionCreate, name="question-create"),
	path('question-update/<str:pk>/', views.questionUpdate, name="question-update"),
	path('question-delete/<str:pk>/', views.questionDelete, name="question-delete"),
	# path('api/<int:pk>/', views.Question_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)