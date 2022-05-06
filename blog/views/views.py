from urllib.request import Request
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from ..modules import BlogEntry
from ..modules import BlogEntryForm
from django.shortcuts import redirect


def post_list(request: Request):
    posts = BlogEntry.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request: Request, pk: int):
    post = get_object_or_404(BlogEntry, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request: Request):
    if request.method == "POST":
        form = BlogEntryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogEntryForm()
    return render(request, 'blog/post_edit.html', {'form': form})
