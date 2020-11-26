from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.encoding import smart_text
from six import python_2_unicode_compatible

urlpatterns = [
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('images/', include('images.urls', namespace='images')),
]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
