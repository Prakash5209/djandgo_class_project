from django.db import models
from django.conf import settings
from post.models import TimeStampModel

class Message(TimeStampModel):
    description = models.TextField()
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = "sent_messages")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = "received_messages")
    
    def __str__(self):
        return str(self.id)
    
    
