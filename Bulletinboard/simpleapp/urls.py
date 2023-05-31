from django.urls import path
from .views import PostList,  AddPost, PostDetailView, PostUpdateView, AddReply, ReplyList, Replyfilter, ReplyDeleteView, AddAcceptReply, AcceptReplyList

urlpatterns = [
    path('', PostList.as_view(), name = 'main'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', AddPost.as_view(), name='create_post'),
    path('<int:pk>/create/', PostUpdateView.as_view(), name='post_update'),
    path('createReply/<int:pk>', AddReply.as_view(), name='reply_create'),
    path('myreply/', ReplyList.as_view(), name = 'my_reply'),
    path('myreply/<slug>', Replyfilter.as_view(), name = 'replyfilter'),
    path('<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply_delete'),
    path('addacceptreply/<int:pk>', AddAcceptReply, name='add_acceptreply'),
    path('myacceptreply/', AcceptReplyList.as_view(), name='myacceptreply')
]