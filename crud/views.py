from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

# CBV
class PostListView(ListView):
    model = Post
    template_name = 'crud/post_list.html'
    context_object_name = 'posts'
    ordering = '-created_at'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['title'] = 'All posts'
        return context

# FBV
def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'crud/post_list.html', context)



def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post':post}
    return render(request, 'crud/post_detail.html', context)
    

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
    post = get_object_or_404(Post, id=id)

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
    return render(request, 'crud/post_update.html', {'form':form, 'post':post})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('post-list')
    
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    return render(request, 'crud/warning.html', {'post':post})