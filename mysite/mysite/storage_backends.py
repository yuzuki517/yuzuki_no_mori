from storages.backends.azure_storage import AzureStorage
from django.conf import settings

class AzureStaticStorage(AzureStorage):
    account_name = settings.AZURE_ACCOUNT_NAME
    account_key = settings.AZURE_ACCOUNT_KEY
    azure_container = settings.AZURE_CONTAINER_STATIC
    expiration_secs = None

class AzureMediaStorage(AzureStorage):
    account_name = settings.AZURE_ACCOUNT_NAME
    account_key = settings.AZURE_ACCOUNT_KEY
    azure_container = settings.AZURE_CONTAINER_MEDIA
