from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    account_name = None 
    account_key = None
    azure_container = None
    expiration_secs = None
    def __init__(self, *args, **kwargs):
        from django.conf import settings
        self.account_name = settings.AZURE_ACCOUNT_NAME
        self.account_key = settings.AZURE_ACCOUNT_KEY
        self.azure_container = settings.AZURE_CONTAINER_STATIC
        super().__init__(*args, **kwargs)

class AzureMediaStorage(AzureStorage):
    account_name = None
    account_key = None
    azure_container = None
    expiration_secs = None

    def __init__(self, *args, **kwargs):
        from django.conf import settings
        self.account_name = settings.AZURE_ACCOUNT_NAME
        self.account_key = settings.AZURE_ACCOUNT_KEY
        self.azure_container = settings.AZURE_CONTAINER_MEDIA
        super().__init__(*args, **kwargs)
