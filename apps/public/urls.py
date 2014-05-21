"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('apps.public',
    # Rest Pattern for Todo Items
    url(r'^api/todo/(?P<user_id>[0-9]+)$', 'views.todo_api', name="create_todo"),

    url(r'^user/id$', 'views.get_current_user_id', name="get_current_user_id"),
    url(r'^todos$', 'views.todos', name="todo_list_html"),
    url(r'^todos-django$', 'views.todos_django', name="todo_list_django"),
    url(r'^todos-django-pure$', 'views.todos_django_pure', name="todo_list_django_pure"),
    url(r'^todos-django-pure/(?P<todo_id>[0-9]+)$', 'views.todos_django_pure_edit', name="todo_edit_django_pure"),
    url(r'^todos-django-pure/add$', 'views.todos_django_pure_add', name="todo_add_django_pure"),
    url(r'^todos-django-pure/delete/(?P<todo_id>[0-9]+)$', 'views.todos_django_pure_delete', name="todo_delete_django_pure"),
    url(r'^logout$', 'views.logout', name="user_logout"),
    url(r'^login$', 'views.login', name="user_login"),
    url(r'^blah$', 'views.blah', name="blah"),
    url(r'^blah2$', 'views.blah2', name="blah2"),
    url(r'^$', 'views.home', name="home"),
)