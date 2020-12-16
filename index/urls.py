from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views as home_views
from index import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index),
    path('create_post/', home_views.create_post),
    path('commented_posts/', home_views.commented_posts),
    path('posts/<int:post_id>/', home_views.post_info),
    path('categories/', home_views.category_chooser),
    path('categories/<int:category_id>/', home_views.category),
    path('like_post/<int:post_id>/', home_views.like_post),
    path('user_posts/', home_views.user_posts),
    path('register/', home_views.register),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', home_views.profile),
    path('accounts/logout/', home_views.logout),
    path('accounts/profile/delete/', home_views.delete_account),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
