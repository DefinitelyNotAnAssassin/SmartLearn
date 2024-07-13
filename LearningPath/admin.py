from django.contrib import admin
from LearningPath.models import LearningPath, LearningPathTopic, StudentLearningPathStatus, StudentLearningPathTopicStatus
# Register your models here.


admin.site.register(LearningPath)
admin.site.register(LearningPathTopic)
admin.site.register(StudentLearningPathStatus)
admin.site.register(StudentLearningPathTopicStatus)