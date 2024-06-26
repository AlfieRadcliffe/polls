from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    # other URL patterns for other apps or custom URLs
]
