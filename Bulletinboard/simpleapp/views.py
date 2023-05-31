from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from Bulletin.models import Post, Category
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from datetime import datetime
from django.core.cache import cache
from simpleapp.forms import PostFormCreate, PostFormUpdate, ReplyForm
from simpleapp.models import Replies, AcceptReply
from django.core.mail import send_mail

class PostList(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'post'
    ordering = ['-datepost']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):
    template_name = 'post.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    permission_required = ('Bulletin.change_post',)
    form_class = PostFormUpdate

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')

class AddPost(PermissionRequiredMixin, CreateView):
    queryset = Post.objects.all()
    template_name = 'post_create.html'
    permission_required = ('Bulletin.add_post',)
    form_class = PostFormCreate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostFormCreate
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddReply(PermissionRequiredMixin, CreateView):
    queryset = Replies.objects.all()
    template_name = 'reply_create.html'
    permission_required = ('simpleapp.add_replies',)
    form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm
        return context
    
    def form_valid(self, form, **kwargs):
        id = self.kwargs.get('pk')
        authorpost = Post.objects.get(pk=id)
        form.instance.replyfrom = self.request.user
        form.instance.replyto = authorpost
        return super().form_valid(form)

class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'reply_delete.html'
    queryset = Replies.objects.all()
    success_url = '/myreply/'
    context_object_name = 'reply'

class ReplyList(ListView):
    model = Replies
    template_name = 'myreply.html'
    context_object_name = 'reply'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['acceptreply'] = AcceptReply.objects.all()
        context['filter'] = self.kwargs.get('slug')
        return context

class Replyfilter(ListView):
    model = Replies
    template_name = 'myreply.html'
    context_object_name = 'reply'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['filter'] = self.kwargs.get('slug')
        return context

def AddAcceptReply(request, pk):
    id = Replies.objects.get(pk=pk)
    replyfrom = id.replyto.author
    replyto = id.replyfrom
    replies = AcceptReply(replies=id)
    replies.save()
    id.isaccepted = True
    id.save(update_fields=["isaccepted"])
    send_mail("Ваш отклик", f'Здравствуйте, ваш отклик на сайте World of Game был принят автором {replyfrom}', None, {replyto.email}, fail_silently=False)
    return redirect("/myacceptreply")

class AcceptReplyList(ListView):
    model = AcceptReply
    template_name = 'myacceptreply.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['acceptreply'] = AcceptReply.objects.all()
        return context




























