from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

questions = []
for i in range(0, 30):
    questions.append({
        'title': 'title ' + str(i),
        'id': i,
        'text': 'text' + str(i)
    })
answers = []
for i in range(0, 30):
    answers.append({
        'text': 'text' + str(i)
    })


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
    page = paginate(questions, request, 10)
    return render(
        request, 'index.html',
        context={'pageTitle': 'New Questions', 'linkTitle': 'Hot Questions', 'link': '/hot', 'logged': True,
                 'questions': page.object_list, 'page_obj': page}
    )


def hot(request):
    hot_questions = []
    for i in range(1, 30):
        hot_questions.append({
            'title': 'hot ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    page = paginate(hot_questions, request, 10)
    return render(
        request, 'index.html',
        context={'pageTitle': 'Hot Questions', 'linkTitle': 'New Questions', 'link': '/', 'logged': True, 'questions': page.object_list,
                 'page_obj': page}
    )


def tag(request, tag_name):
    tag_questions = []
    for i in range(0, 7):
        tag_questions.append({
            'title': 'tag ' + str(i),
            'id': i,
            'text': tag_name + str(i)
        })
    page = paginate(tag_questions, request, 5)
    return render(
        request, 'index.html',
        context={'pageTitle': 'Tag', 'linkTitle': tag_name, 'link': '#', 'logged': True, 'questions': page.object_list,
                 'page_obj': page}
    )


def question(request, question_id):
    one_question = questions[question_id]
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
