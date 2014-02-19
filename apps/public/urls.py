"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('apps.public',
    url(r'^api/todos$', 'views.todos', name="todo_list"),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
)