from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class LangChoice(models.TextChoices):
    C = ("C","C")
    Cpp = ("C++","C++")
    Python = ("python","Python")
    Javascript = ("javascript","Javascript")
    Java = ("java","Java")
    Go = ("go","Go")
    Rust = ("rust","rust")

class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    question = models.TextField()
    answer  = models.TextField()
    id = models.CharField(default=uuid.uuid4,max_length=100,primary_key=True,editable=False)
    language = models.CharField(choices=LangChoice,default="",max_length=110)
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
    
