from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from home import views as home_views
from index import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index),
    path('login/', home_views.login),
    path('register/', home_views.register),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
