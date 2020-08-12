from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.api.v1.urls')),
    # docs urls
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)