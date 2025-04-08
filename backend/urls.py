from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", lambda request: redirect("admin/", permanent=False)),
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blogs.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
