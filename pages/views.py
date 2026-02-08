from django.views.generic import TemplateView
from blog.models import Post

class ContactView(TemplateView):
    template_name = "pages/contact.html"

class SiteMapView(TemplateView):
    template_name = "pages/site_map.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-created_at")
        return context

class PrivacyView(TemplateView):
    template_name = "pages/privacy.html"

