from django.shortcuts import render
from LearningPath.models import LearningPath, LearningPathTopic, StudentLearningPathStatus, StudentLearningPathTopicStatus

# Create your views here.


def index(request): 
    return render(request, 'LearningPath/index.html')

def learning_path(request, learning_path_code):
    path = LearningPath.objects.get(path_code = learning_path_code) 
    topics = LearningPathTopic.objects.filter(learning_path = path)
    items = { 
             'path': path,
             'topics': topics
             }

    return render(request, 'LearningPath/view_path.html', context = items)


def my_paths(request):
   
    items = { 
             'paths': StudentLearningPathStatus.objects.filter(student = request.user)
             }
    return render(request, 'LearningPath/my_paths.html', context = items)