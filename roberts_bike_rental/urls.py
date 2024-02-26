from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", TemplateView.as_view(template_name="index.html"), name="index-page"),

    # path("home", TemplateView.as_view(template_name="index.html"), name="index-page"),

    path("about-roberts-rentals", TemplateView.as_view(template_name="about.html"), name="about-roberts-rentals"),

    path("bike-accessories", TemplateView.as_view(template_name="accessories.html"), name="bike-accessories-page"),

    path('bike/', include('bike.urls')), 

    path("accounts/", include("accounts.urls")),

    path("accounts/", include("django.contrib.auth.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
