from django import forms
from .models import *
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question","answer","language"]
        labels = {
            "language":"Select programming Language"
        }

        widgets = {
            "question": forms.Textarea(attrs={"class":"textarea card text-black  textarea-bordered bg-white  font-bold w-full","placeholder":"Enter the Question","style":"height: 7rem;"}),
            "answer": forms.Textarea(attrs={"class":"textarea text-black  textarea-bordered card  bg-white font-bold w-full  ","placeholder":"Enter the Answer","style":"height: 10rem;"}),
            "language" : forms.Select(attrs={"class":"text-black font-bold"})
        }