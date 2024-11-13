from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from app.models import Question, Answer


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    try:
        page_num = request.GET.get('page', 1)
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def index(request):
    new_questions = Question.objects.get_new()
    page = paginate(new_questions, request, 10)
    return render(
        request, 'index.html',
        context={'pageTitle': 'New Questions', 'linkTitle': 'Hot Questions', 'link': '/hot', 'logged': True,
                 'questions': page.object_list, 'page_obj': page}
    )


def hot(request):
    hot_questions = Question.objects.get_hot()
    page = paginate(hot_questions, request, 10)
    return render(
        request, 'index.html',
        context={'pageTitle': 'Hot Questions', 'linkTitle': 'New Questions', 'link': '/', 'logged': True,
                 'questions': page.object_list,
                 'page_obj': page}
    )


def tag(request, tag_name):
    tag_questions = Question.objects.get_with_tag(tag_name)
    page = paginate(tag_questions, request, 5)
    return render(
        request, 'index.html',
        context={'pageTitle': 'Tag', 'linkTitle': tag_name, 'logged': True, 'questions': page.object_list,
                 'page_obj': page}
    )


def question(request, question_id):
    one_question = Question.objects.get_one_question(question_id)
    answers = Answer.objects.get_answers(one_question)
    page = paginate(answers, request, 5)
    return render(
        request, 'question.html',
        context={'question': one_question, 'logged': True, 'answers': page.object_list, 'page_obj': page}
    )


def login(request):
    return render(
        request, 'login.html',
        context={'logged': False}
    )


def signup(request):
    return render(
        request, 'signup.html',
        context={'logged': False}
    )


def ask(request):
    return render(
        request, 'ask.html',
        context={'logged': True}
    )
