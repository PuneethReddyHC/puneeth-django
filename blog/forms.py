from blog.models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title', 'slug', 'content','status')
        widgets = {
            'content': SummernoteWidget(),
        }

    def is_valid(self):
        valid = super(CreatePostForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        Post = super(CreatePostForm, self).save(commit=False)
        if commit:
            Post.save()
        return Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')