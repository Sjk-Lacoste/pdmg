from django.db import models
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import CommentForm


# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'
    paginate_by = 5


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by('-created_on')
    new_comment = None
    categories = Category.objects.annotate(num_posts=models.Count('post')).all()

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)

            # Assign the current post to the comment
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'categories': categories
    }
    return render(request, template_name, context)

def category_view(request):
    pass
