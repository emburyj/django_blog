from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from myblog.models import Post, Category

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    cats = Category.objects.all()
    context = {'posts': posts, 'cats': cats}
    return render(request, 'list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    cats = Category.objects.all()
    context = {'post': post, 'cats': cats}
    return render(request, 'detail.html', context)

def cat_view(request, category_id):
    published = Post.objects.exclude(published_date__exact=None)
    cat_published = published.filter(categories__exact=category_id)
    posts = cat_published.order_by('-published_date')
    # posts = published.order_by('-published_date')
    cats = Category.objects.all()
    cat_select = cats.filter(id__exact=category_id)
    context = {'posts': posts, 'cats': cats, 'cat_posts': cat_select}
    return render(request, 'list.html', context)