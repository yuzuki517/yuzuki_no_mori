from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    azure_container = "yuzuki-static"
    expiration_secs = None

class AzureMediaStorage(AzureStorage):
    azure_container = "yuzuki-media"
    expiration_secs = None

