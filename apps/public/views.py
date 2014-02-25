from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from json import dumps

from .models import Todo


# Found at https://docs.djangoproject.com/en/dev/topics/http/decorators/
@require_http_methods(["GET"])
def todos(request):
    # Found at https://docs.djangoproject.com/en/dev/topics/serialization/
    data = serializers.serialize("json", Todo.objects.all())
    return HttpResponse(data, mimetype="application/json")


@require_http_methods(["POST", "OPTIONS"])
def todo(request):
    if request.method == "POST":
        from datetime import datetime
        Todo.objects.create(title=request.POST['todoTitle'], create_date=datetime.now())
    elif request.method == "PUT":
        todo = Todo()
        todo.id = request.PUT['id']
        todo.title = request.PUT['title']
        todo.description = request.PUT['description']
        todo.create_date = request.PUT['create_date']
        todo.save()

    data = serializers.serialize("json", Todo.objects.all())
    return HttpResponse(data, mimetype="application/json")