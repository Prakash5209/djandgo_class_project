from django import forms
from post.models import Post,Comment

# class PostForm(forms.Form):
#     description=forms.CharField(widget=forms.Textarea)
#     image = forms.ImageField(widget=forms.ClearableFileInput,required=False)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('description','image','status')
        # exclude = ('user',)
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description.isnumeric():
            raise forms.ValidationError('post can not be number')
        return description
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("description",)
        