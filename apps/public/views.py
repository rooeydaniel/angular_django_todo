from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from json import dumps
from json import loads
from urlparse import parse_qs

from django.contrib.auth.models import User
from .models import Todo

@require_http_methods(["GET", "POST", "PUT", "DELETE", "OPTIONS"])
def todo_api(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == "POST":
        from datetime import datetime

        title = request.POST['title'] if request.POST.has_key('title') else None
        description = request.POST['description'] if request.POST.has_key('description') else None

        if '&' not in request.body:
            json = loads(request.body)

            if json.has_key('title'):
                title = json['title']
            if json.has_key('description'):
                description = json['description']

        Todo.objects.create(title=title, description=description, create_date=datetime.now(), user=user)
    elif request.method == "PUT":
        todo = None
        if request.body and '&' in request.body:
            data = parse_qs(request.body)

            todo = Todo.objects.get(pk=data['id'][0])
            todo.title = data['title'][0] if data.has_key('title') else todo.title
            todo.description = data['description'][0] if data.has_key('description') else todo.description

            if data.has_key('completed'):
                if data['completed'][0] == 'true':
                    todo.completed = 1
                else:
                    todo.completed = 0
        else:
            json = loads(request.body)

            todo = Todo.objects.get(pk=json['id'])

            if json.has_key('title'):
                todo.title = json['title']
            if json.has_key('description'):
                todo.description = json['description']
            if json.has_key('completed'):
                todo.completed = json['completed']

        todo.save()
    elif request.method == "DELETE":
        todo_id = request.REQUEST['id'] if request.REQUEST.has_key('id') else parse_qs(request.body)['id'][0]
        todo = Todo.objects.get(pk=todo_id)

        todo.delete()

    data = serializers.serialize("json", Todo.objects.filter(user_id=user_id).order_by('create_date'))
    return HttpResponse(data, content_type="application/json")


# Django Views
@login_required(function=None, redirect_field_name=None, login_url='/login')
@require_http_methods(["GET"])
def todos(request):
    response = {}
    user = request.user
    response['todos'] = Todo.objects.filter(user_id=user.id).order_by('create_date')
    return render(request, 'partials/todo.tpl.html', response)


@login_required(function=None, redirect_field_name=None, login_url='/login')
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


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
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
    else:
        user = request.user
        if user is not None and user.is_active:
            return redirect('/')
        return render(request, 'partials/login.tpl.html')


@login_required(function=None, redirect_field_name=None, login_url='/login')
@require_http_methods(["GET"])
def logout(request):
    response = {}
    auth.logout(request)

    response['message'] = 'Logout successful!'
    return render(request, 'partials/login.tpl.html', response)


@login_required(function=None, redirect_field_name=None, login_url='/login')
@require_http_methods(["GET"])
def home(request):
    return render(request, 'partials/home.tpl.html')