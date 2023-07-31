from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

api_paths = [
    path('basics/', include('basic.urls')),
    path('accounts/', include('accounts.urls')),
    path('supports/', include('support.urls')),
    path('clubs/', include('club.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/v1/', include(api_paths)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
