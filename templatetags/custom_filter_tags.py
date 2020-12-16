from django import template

from home.models import Post

register = template.Library()


@register.filter
def count_posts_in_category(category):
    posts_in_category = Post.objects.filter(category=category)
    return len(posts_in_category)


@register.filter
def count_user_posts_in_category(category, user):
   user_posts_in_category = Post.objects.filter(category=category, user=user)
   return len(user_posts_in_category)
