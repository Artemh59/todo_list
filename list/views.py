from django.views import generic
from django.urls import reverse_lazy

from list.models import Task, Tag


class Index(generic.ListView):
    model = Task
    ordering = ['done', '-datetime']


class TaskCreateView(generic.CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('list:index')


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('list:index')


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('list:index')


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('list:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('list:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('list:tag-list')
