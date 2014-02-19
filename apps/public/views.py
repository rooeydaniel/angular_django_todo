from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(('GET',))
def todos(request):
    todos = [{'title': 'Test One'}, {'title': 'Test Two'}, {'title': 'Test Three'}]
    return JSONResponse(todos)