from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('account/', include('account.urls', namespace='account')),
    path('post/', include('post.urls', namespace='post')),
    path('category/', include('category.urls', namespace='category')),
    path('activity/', include('activity.urls', namespace='activity')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
