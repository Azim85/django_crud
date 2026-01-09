from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'crud/post_list.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post':post}
    return render(request, 'crud/post_detail.html', context)
    
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post.get_absolute_url())
    form = PostForm()
    return render(request, 'crud/post_create.html', {'form':form})

def post_update(request, id):
    post = Post.objects.get(id=id)

    if post.author != request.user:
        return redirect('post-list')
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post.get_absolute_url())
    form = PostForm(instance=post)
    return render(request, 'crud/post_update.html', {'form':form})


def post_delete(request):
    pass