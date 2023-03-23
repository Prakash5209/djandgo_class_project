from django.db import models
from django.conf import settings

class Status(models.TextChoices):
    DRAFT  = 'draft','DRAFT',
    PUBLIC = 'public','PUBLIC',


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
    
class Post(TimeStampModel):
    description = models.TextField()
    image = models.ImageField(upload_to='posts',blank = True,null = True)
    status = models.CharField(max_length = 100,choices=Status.choices,default=Status.DRAFT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank = True,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def likes_count(self):
        return self.likes.filter(is_liked = True).count()
    
    # class Meta:
    #     ordering = ['-created_at',]
    
class Comment(TimeStampModel):
    description = models.CharField(max_length=255)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name = 'comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank = True,null=True)
    
    def __str__(self):
        return str(self.id)
    
class Like(TimeStampModel):
    is_liked = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank = True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name = 'likes')
    def __str__(self):
        return str(self.id)