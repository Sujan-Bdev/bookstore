from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
