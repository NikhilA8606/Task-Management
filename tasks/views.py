from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView, View

from tasks.models import Task

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.forms import ModelForm



class TaskCreateForm(ModelForm):

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 10:
            raise ValidationError("Title is too small")
        return title.upper()
    class Meta:
        model = Task
        fields = ["title","description","completed"]

class GenericTaskCreateView(CreateView):
    form_class = TaskCreateForm
    template_name = "task_create.html"
    success_url = "/task"

class GenericTaskUpdateView(UpdateView):
    model = Task     
    form_class = TaskCreateForm
    template_name = 'task_update.html'
    success_url = '/task'

class GenericTaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

class GenericTaskView(ListView):
    queryset = Task.objects.filter(deleted_data=False)
    template_name = 'task.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        search_item = self.request.GET.get("search")
        tasks = Task.objects.filter(deleted_data=False)
        if search_item:
            tasks = tasks.filter(title__icontains=search_item)
        return tasks
    
class CreateTaskView(View):
    def get(self,request):
        return render(request,'task_create.html')
    
    def post(self,request):
        task_value = request.POST.get('task')
        task_obj = Task(title=task_value)
        task_obj.save()
        return HttpResponseRedirect('/task')



class TaskView(View):
    def get(self,request):
        search_item = request.GET.get("search")
        tasks = Task.objects.filter(deleted_data=False)
        if search_item:
            tasks = tasks.filter(title__icontains=search_item)
        return render(request,'task.html',{'tasks': tasks})
    def post(self,request):
        pass


def task_view(request):
    search_item = request.GET.get("search")
    tasks = Task.objects.filter(deleted_data=False)
    if search_item:
        tasks = tasks.filter(title__icontains=search_item)
    return render(request,'task.html',{'tasks': tasks})

def add_task_view(request):
    task_value = request.GET.get('task')
    task_obj = Task(title=task_value)
    task_obj.save()
    return HttpResponseRedirect('/task')

def delete_task_view(request,index):
    Task.objects.filter(id=index).update(deleted_data=True)
    return HttpResponseRedirect('/task')

# def add_com_task_view(response):
#     completed = response.GET.get('task')
#     comp_tasks.append(completed)
#     return HttpResponseRedirect('/task')

# def delete_comp_task_view(response,val):
#     res = comp_tasks[val-1]
#     tasks.remove(res)
#     return HttpResponseRedirect('/task')
