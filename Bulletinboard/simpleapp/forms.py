from django.forms import ModelForm
from Bulletin.models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from simpleapp.models import Replies

class PostFormCreate(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'textpost', 'image', 'video', 'categorypost']

class PostFormUpdate(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'textpost', 'image', 'video', 'categorypost']

class ReplyForm(ModelForm):
    class Meta:
        model = Replies
        fields = ['textreply']



class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        author_group = Group.objects.get(name='author')
        author_group.user_set.add(user)
        return user

































































