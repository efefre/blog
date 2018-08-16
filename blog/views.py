from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models  # other version: from .models import Post
from django.views.generic import ListView


# Create your views here.
class PostListView(ListView):
    queryset = models.Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = 'blog/post/list.html'

# def post_list(request):
#     object_list = models.Post.published.all()
#     paginator = Paginator(object_list, 3)  # Three posts in each page
#     page = request.GET.get('strona')  # 'strona' was used in pagination.html
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html',
#                   {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(models.Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html',
                  {'post': post})
