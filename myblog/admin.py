from django.contrib import admin
from myblog.models import Post, Category
from django.urls import reverse
from django.utils.html import format_html
from datetime import datetime as dt

# admin.site.register(Post)
# admin.site.register(Category)

class CategoryInline(admin.StackedInline):
    model = Category.posts.through

@admin.action(description="Publish selected posts")
def make_published(modeladmin, request, queryset):
    queryset.update(published_date=dt.utcnow())

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ('title', 'text', 'author', 'published_date')})]
    readonly_fields = ('title',)
    list_display = ('title','author_for_admin','created_date', 'modified_date')
    inlines = [CategoryInline]

    actions = [make_published]

    def author_for_admin(self, obj):
        author = obj.author
        url = reverse('admin:auth_user_change', args=(author.pk,))
        name = author.get_full_name() or author.username
        link = f"<a href=\"{url}\">{name}</a>"
        return format_html(link)
    author_for_admin.short_description = 'Author'
    author_for_admin.allow_tags = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']
