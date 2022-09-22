from django.shortcuts import render, redirect
from miapp.models import Post
from .forms import PostForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home(request):
    return render(request, 'post/index.html',
                  {'posts':Post.objects.count(),
                   'dato': 22
                   })


def post_list(request):
    #posts = Post.objects.all()
    #posts = Post.objects.filter(
    #    status = 'published'
    #)

    object_list = Post.objects.filter(
        status = 'published'
    )

    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/post_list.html',
                  {'posts': posts})


def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            #redirect("post_list")
    else:
        form = PostForm
    return render(request, 'post/newpost.html', {'form': form})
