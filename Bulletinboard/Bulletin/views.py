from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from Bulletin.models import Post
from django.contrib.auth.mixins import PermissionRequiredMixin

class Post(View):

    def get(self, request):
        post = Post.objects.order_by('-datepost')
        p = Paginator(post, 10)
        post = p.get_page(request.GET.get('page', 1))
        data = {
            'post': post,
        }
        return render(request, 'main.html', data)



































































