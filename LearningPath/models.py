from django.db import models
from uuid import uuid4
# Create your models here.

class LearningPath(models.Model): 
    path_code = models.CharField(max_length=256, default = str(uuid4())[:7], editable=False)
    name = models.CharField(max_length=100)    
    description = models.CharField(max_length=500)    
    image = models.ImageField(upload_to='images/', blank  = True, null = True)    
    level = models.ForeignKey('Level.Level', on_delete=models.CASCADE)
    def __str__(self):        
        return self.name
    
    
class LearningPathTopic(models.Model):    

    learning_path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)    
    topic_name = models.CharField(max_length=100) 
    topic_description = models.TextField()

    order = models.PositiveIntegerField(default = 0)
    topic_image = models.ImageField(upload_to='images/', blank  = True, null = True)
    
    def __str__(self):        
        return self.learning_path.name + ' - ' + self.topic_name 
    

class StudentLearningPathStatus(models.Model):
    PATH_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('not_started', 'Not Started'),
    )
    student = models.ForeignKey('UserAuthentication.Account', on_delete=models.CASCADE)
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,  choices=PATH_STATUS)
    def __str__(self):        
        return self.student.username + ' - ' + self.path.name

class StudentLearningPathTopicStatus(models.Model):
    TOPIC_STATUS = (
        
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('not_started', 'Not Started'),
    )
    student = models.ForeignKey('UserAuthentication.Account', on_delete=models.CASCADE)
    topic = models.ForeignKey(LearningPathTopic, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,  choices=TOPIC_STATUS)
    def __str__(self):        
        return self.student.username + ' - ' + self.topic.topic_name    


class LearningPathActivity(models.Model): 
    
    ACTIVITIES = ( 
        ('video', 'Video'), 
        ('quiz', 'Quiz'),
        ('assessment', 'Assessment'),
        ('assignment', 'Assignment'),
        ('discussion', 'Discussion'),
        ('reading', 'Reading'),
        ('exercise', 'Exercise'),
        ('project', 'Project'),
        ('lab', 'Lab'),)
    topic = models.ForeignKey(LearningPathTopic, on_delete=models.CASCADE)    
    activity_name = models.CharField(max_length=100)    
    activity_description = models.TextField()    
    activity_type = models.CharField(max_length=100, choices=ACTIVITIES, default='video')      
    order = models.PositiveIntegerField(default = 0)    
    student = models.ForeignKey('UserAuthentication.Account', on_delete=models.CASCADE, null = True, blank = True)
    questions = models.JSONField(default=dict, blank=True)  # {question_number: question}
    def __str__(self):        
        return self.topic.topic_name + ' - ' + self.activity_name
    
    

  