from django import forms
from chat.models import Message

class ChatForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("description",)