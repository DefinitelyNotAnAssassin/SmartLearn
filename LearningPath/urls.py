from django.urls import path  
from LearningPath import views 



urlpatterns = [ 
               path('', views.index, name = 'learning path home'),
               path('path/<str:learning_path_code>', views.learning_path, name = 'learning_path'),
               path('my_paths/', views.my_paths, name = 'my paths'),
               ]