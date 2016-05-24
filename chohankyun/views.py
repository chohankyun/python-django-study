from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from chohankyun.models import User


class DetailUser(DetailView):
    model = User
    template_name = 'chohankyun/user_form.html'


class ListUser(ListView):
    model = User
    paginate_by = 1
    template_name = 'user_list.html'


class CreateUser(CreateView):
    model = User
    fields = ['name', 'address', 'phone']
    success_url = '/chohankyun/'


class UpdateUser(UpdateView):
    model = User
    fields = ['name', 'address', 'phone']
    success_url = '/chohankyun/'


class DeleteUser(DeleteView):
    model = User
    success_url = '/chohankyun/'
