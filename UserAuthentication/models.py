from django.db import models
from django.contrib.auth.models import AbstractUser 
from uuid import uuid4


class Account(AbstractUser): 
    ROLES = ( 
        ('student', 'Student'), 
        ('teacher', 'Teacher'), 
        ('admin', 'Admin'), 
    )
    role = models.CharField(max_length=100, choices=ROLES, default='student')
    uuid = models.UUIDField(unique=True, editable=False, default = uuid4())
    
    
    
