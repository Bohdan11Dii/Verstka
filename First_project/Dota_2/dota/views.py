
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from dota.models import Heroy
from dota.utils import DataMixin

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contact', 'url_name': 'contact'},

        ]

def index(request):
    posts = Heroy.objects.all
    context = {
        'posts': posts,
        'menu': menu,

    }

    return render(request, 'dota/index.html', context=context)


def about(request):
    return render(request, 'dota/about.html')


def home(request):
    return render(request, 'dota/home.html')


def contact(request):
    return render(request, 'dota/contact.html')


def login(request):
    return HttpResponse("Authorization")


def show_post(reqyest, post_id):
    return HttpResponse(f"Heroyes with id = {post_id}")


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'dota/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="registration")
        return dict(list(context.items()) + list(c_def.items()))


