from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from blog.models import Post
from .forms import ContactForm

class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("pages:contact_done")

    def form_valid(self, form):
        send_mail(
            subject=form.cleaned_data["subject"],
            message=(f"名前: {form.cleaned_data['name']}\n"
                     f"メールアドレス: {form.cleaned_data['email']}\n\n"
                     f"{form.cleaned_data['message']}"),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
        )
        return super().form_valid(form)

class ContactDoneView(TemplateView):
    template_name = "pages/contact_done.html"

class SiteMapView(TemplateView):
    template_name = "pages/site_map.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by("-created_at")[:10]
        return context

class PrivacyView(TemplateView):
    template_name = "pages/privacy.html"

