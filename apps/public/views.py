from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.contrib import auth
from django.core.context_processors import csrf
from json import dumps
from json import loads

from django.contrib.auth.models import User
from .models import Todo

# REST API Views
# Found at https://docs.djangoproject.com/en/dev/topics/http/decorators/
@require_http_methods(["GET"])
def todos_api(request, user_id):
    data = serializers.serialize("json", Todo.objects.filter(user_id=user_id).order_by('create_date'))
    return HttpResponse(data, content_type="application/json")


@require_http_methods(["POST", "OPTIONS"])
def todo_api(request, user_id):
    user = User.objects.get(pk=user_id)

    json = loads(request.body)
    title = json['title']

    if request.method == "POST":
        from datetime import datetime

        Todo.objects.create(title=title, create_date=datetime.now(), user=user)
    elif request.method == "PUT":
        todo = Todo.objects.get(pk=request.PUT['id'])
        todo.user = User.objects.get(pk=request.PUT['user_id'])
        todo.title = title
        todo.description = json['description']
        todo.save()

    data = serializers.serialize("json", Todo.objects.filter(user_id=user_id).order_by('create_date'))
    return HttpResponse(data, content_type="application/json")


# Django Views
@require_http_methods(["GET"])
def todos(request):
    return render(request, 'partials/todo.tpl.html')


@require_http_methods(["GET"])
def get_current_user_id(request):
    user = [{'user_id': request.user.id}]
    return HttpResponse(dumps(user), content_type="application/json")


@require_http_methods(["POST"])
def authenticate(request):
    response = {}
    response.update(csrf(request))

    username = request.POST.get('username', request.POST['username'])  # emtpy string if no username exists
    password = request.POST.get('password', request.POST['password'])  # empty string if no password exists

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        request.session['test'] = 'Testing, Testing'
        return redirect('/', response)
    else:
        response['message'] = 'Login failed!'
        return render(request, 'partials/login.tpl.html', response)


@require_http_methods(["GET"])
def login(request):
    user = request.user
    if user is not None and user.is_active:
        return redirect('/')
    return render(request, 'partials/login.tpl.html')


@require_http_methods(["GET"])
def logout(request):
    response = {}
    auth.logout(request)

    response['message'] = 'Logout successful!'
    return render(request, 'partials/login.tpl.html', response)


@require_http_methods(["GET"])
def home(request):
    user = request.user
    if user is None or not user.is_active:
        return redirect('/login')
    return render(request, 'partials/home.tpl.html')