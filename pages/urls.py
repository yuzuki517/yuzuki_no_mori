from django.urls import path
from .views import ContactView, SiteMapView, PrivacyView

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("site-map/", SiteMapView.as_view(), name="site_map"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
]
