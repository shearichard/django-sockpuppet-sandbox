from django.views.generic.base import TemplateView
from .mixins import ToDoMixin


class TodoReflexView(ToDoMixin, TemplateView):
    template_name = 'todo_reflex.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = 0
        return context


todoreflexview = TodoReflexView.as_view()    
