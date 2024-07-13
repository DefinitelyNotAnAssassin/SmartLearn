from django.db import models

# Create your models here.


class LearnerProfile(models.Model):
    user = models.OneToOneField("UserAuthentication.Account", on_delete=models.CASCADE) 
    level = models.ForeignKey("Level.Level", on_delete=models.SET_NULL, null=True, blank=True)
    learning_style = models.CharField(max_length=50, choices=[
        ('visual', 'Visual'),
        ('auditory', 'Auditory'),
        ('kinesthetic', 'Kinesthetic'),
    ], null=True, blank=True)  # Add more as needed

    # Progress and Performance
    completed_topics = models.ManyToManyField("LearningPath.LearningPathTopic", blank=True)
    quiz_scores = models.JSONField(default=dict, blank=True)  # {quiz_id: score}
    assessment_results = models.JSONField(default=dict, blank=True)  # {assessment_id: result}
    # Preferences and Interests
    preferred_topics = models.ManyToManyField("LearningPath.LearningPath", blank=True, related_name='preferred_by')
    interests = models.TextField(blank=True)  # Free-form text
    goals = models.TextField(blank=True)  # What the learner wants to achieve
    
    # Additional Information
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    feedback = models.TextField(blank=True)  # Learner's feedback on the platform
    
    def __str__(self):
        return f"Profile for {self.user.username}"
