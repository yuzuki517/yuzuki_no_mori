from django.urls import path
from .views import ContactView, ContactDoneView, SiteMapView, PrivacyView

urlpatterns = [
    path("contact/done/", ContactDoneView.as_view(), name="contact_done"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("site-map/", SiteMapView.as_view(), name="site_map"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
]
