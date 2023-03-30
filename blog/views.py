from typing import ContextManager
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from .models import Blog, BlogCategory, Comment
from .forms import CommentForm
from django.views.generic.edit import CreateView, FormMixin, FormView,ModelFormMixin
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = Blog.objects.filter(is_published=True).order_by('-id')
        context['popular_posts'] = Blog.objects.order_by('-view_count')[:4]
        context['categories'] = BlogCategory.objects.all()[:5]
        return context


class BlogDetailView(FormMixin, DetailView):
    template_name = 'blog_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.object.pk})

    def get_object(self):
        return Blog.objects.filter(id=self.kwargs['pk']).first()

    def update_view_count(self):
        obj = self.get_object()
        obj.view_count += 1
        obj.save()

    def get(self, request, *args, **kwargs):
        self.update_view_count()
        context = {
            'object' : self.get_object(),
            'popular_posts' : Blog.objects.order_by('-view_count')[:4],
            'categories' : BlogCategory.objects.all()[:5],
            'blog_comments' : self.get_object().comments.all(),
            'form' : self.get_form
        }
        return render(request, 'blog_detail.html', context=context)

    def create_comment(self, **kwargs):
        blog=Blog.objects.get(pk=kwargs.get('blog'))
        return Comment.objects.create(
            blog=blog,
            name=kwargs.get('name'),
            email=kwargs.get('email'),
            comment=kwargs.get('comment')
        )

    def post(self, request, **kwargs):
        self.object = self.get_object()
        form = self.get_form()  

        if form.is_valid():
            self.create_comment(
                blog=kwargs.get('pk'),
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                comment=form.cleaned_data.get('comment')
            )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        return super().post(request,  **kwargs)



def category_list(request,id):
    category = BlogCategory.objects.get(id=id)
    category_blogs = category.blogs.all()
    context = {
        'category_blogs' : category_blogs,
        'popular_posts' : Blog.objects.order_by('-view_count')[:4],
        'categories' : BlogCategory.objects.all()[:5]
    }
    return render(request, 'blog.html', context)



# def BlogDetail(request):
#     return render(request, 'blog_detail.html')