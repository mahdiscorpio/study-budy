from django.forms import ModelForm
from .models import Message, Room
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


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
