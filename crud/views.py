from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'crud/post_list.html', context)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request, 'crud/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(post.get_absolute_url())
    form = PostForm()
    return render(request, 'crud/post_create.html', {'form':form})

def post_update(request):
    pass

def post_delete(request):
    pass