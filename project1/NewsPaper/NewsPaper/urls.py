from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('', include('news.urls')),
   path("accounts/", include("django.contrib.auth.urls")),
   path('accounts/', include("allauth.urls")),

]