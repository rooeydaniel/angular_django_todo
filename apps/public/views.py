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
    # return HttpResponse(data, mimetype="application/json")

    new_data = [{'title': 'test todo one'}, {'title': 'test todo two'}]
    return HttpResponse(dumps(new_data), mimetype="application/json")