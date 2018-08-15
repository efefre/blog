from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models


# Create your views here.
def post_list(request):
    object_list = models.Post.published.all()
    paginator = Paginator(object_list, 3)  # Three posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)    
    return render(request, 'blog/post/list.html', {'page':page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(models.Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html',
                  {'post': post})
