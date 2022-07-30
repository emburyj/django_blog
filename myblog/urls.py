from django.urls import path, re_path
from myblog.views import stub_view
from myblog.views import list_view, detail_view, cat_view

urlpatterns = [
    re_path(r'^$',
        list_view,
        name="blog_index"),
    re_path(r'^posts/(?P<post_id>\d+)/$',
            detail_view,
            name="blog_detail"),
    re_path(r'^category/(?P<category_id>\d+)/$',
            cat_view,
            name="blog_cat")
]