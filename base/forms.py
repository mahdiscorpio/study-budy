from django.forms import ModelForm
from .models import Message, Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


# only used in updateMessage view
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
