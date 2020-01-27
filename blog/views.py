from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from jobsapp.decorators import user_is_employer
from blog.forms import CreatePostForm
from blog.models import Post

from accounts.models import User
from django import forms
from django.shortcuts import render
from django_summernote.widgets import SummernoteWidget
class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blogs.html"
    paginate_by = 3
STATUS = ((0, "Draft"), (1, "Publish"))
 
def index(request):
    passed = False
    form = CreatePostForm()

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            passed = True
            form = CreatePostForm()

    return render(request, 'create.html', {
        'passed': passed,
        'Post_form': form,
    })
    
def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

