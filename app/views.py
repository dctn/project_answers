from django.shortcuts import HttpResponse,render,get_object_or_404,redirect
from django.http import JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound
import datetime 
# Create your views here.
def index(request):
    all_questions = Question.objects.all().order_by("uploaded_at")

    if request.method == "POST":
        word = request.POST.get("search")
        all_questions = Question.objects.filter(question__icontains=word)
        if not all_questions:
            messages.error(request,"Question not found")
            return redirect("home")

    paginator = Paginator(all_questions,5)
    page = int(request.GET.get("page",1))
    try:
        all_questions = paginator.page(page)
    except:
        return HttpResponse("")

    context = {
        "questions":all_questions,
        "page":page,
    }
    if request.headers.get("HX-Request"):
        return render(request,"infinite.html",context)
    return render(request,"index.html",context)

@login_required
def answer(request,question_id):
    q_and_a = get_object_or_404(Question,id=question_id)

    context = {
        "question":q_and_a
    }

    return render(request,"answer.html",context)

def about(request):

    return render(request,"about.html")

@login_required
def create(request):
    form =  QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)

            try:
                name = guess_lexer(data.answer)
                print(name.name)
            except ClassNotFound:
                print("it is not a programming language")
            if name.name != "Text only":
                data.user = request.user
                data.save()
                return redirect("answer",data.id)
            messages.error(request,"your input is  not programming language")
            return redirect("home")
    context = {
        "form":form
    }
    return render(request,"create.html",context)

def delete_question(request,question_id):
    question =  get_object_or_404(Question,id=question_id)
    question.delete()

    return redirect("home")