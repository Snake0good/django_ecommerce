from django.contrib import admin
from django.urls import path, include

from core.views import *

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
]
