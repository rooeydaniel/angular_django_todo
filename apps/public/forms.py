from .models import Todo
from django.forms import ModelForm


class EditTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('user', 'title', 'description', 'completed',)

    def __init__(self, *args, **kwargs):
        super(EditTodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})


class AddTodoForm(ModelForm):
    class Meta:
        model = Todo

    def __init__(self, *args, **kwargs):
        super(AddTodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})
        self.fields['create_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'MM/DD/YYYY'})


class DeleteTodoForm(ModelForm):
    class Meta:
        model = Todo