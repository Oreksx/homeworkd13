from django_filters import FilterSet
from simpleapp.models import Replies
 
 

class ReplyFilter(FilterSet):
    class Meta:
        model = Replies
        fields = ('textreply', 'replyfrom', 'replyto')