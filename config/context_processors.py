# config/context_processors.py
from django.conf import settings

def ga_settings(request):
    return {
        "GA_MEASUREMENT_ID": settings.GA_MEASUREMENT_ID,
        "debug": settings.DEBUG,
    }
