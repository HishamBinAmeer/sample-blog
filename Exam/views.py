from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
# from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.all()
    # Post.objects.get(pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})
    # def post_detail(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    # return render(request, 'blog/post_detail.html', {'post': post})
    def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})