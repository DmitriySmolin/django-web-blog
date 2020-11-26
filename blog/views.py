from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News


# def home(request):
#     data = {
#         'news': News.objects.all(),
#         'title': 'Главная страница блога'
#     }
#     return render(request, 'blog/home.html', data)


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница блога'
        return ctx


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'post'
    template_name = 'blog/news_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страница про нас'})
