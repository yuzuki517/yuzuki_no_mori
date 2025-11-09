"""
Django settings for yuzuki-no-mori project.
Blob ストレージ（Azure Blob）を利用する構成。
"""

from pathlib import Path
import os
import environ

# --- 基本パスと env 読み込み ---
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
)
# プロジェクトルートの .env を読み込む
env.read_env(BASE_DIR / ".env")

# --- セキュリティ / デバッグ ---
DEBUG = env.bool("DEBUG", default=False)

if DEBUG:
    SECRET_KEY = env("SECRET_KEY", default="dev-secret-key")
else:
    SECRET_KEY = env("SECRET_KEY")

# ALLOWED_HOSTS の読み込みと WEBSITE_HOSTNAME の自動追加
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
_website_hostname = env("WEBSITE_HOSTNAME", default=None)
if _website_hostname and _website_hostname not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(_website_hostname)

# --- アプリケーション定義 ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # サードパーティ
    "storages",  # django-storages を使う
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise を先に入れておく
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"

# --- データベース ---
DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# --- パスワードバリデータ（デフォルト） ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- 国際化 ---
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --- デフォルトの自動フィールド ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Azure Blob 関連の環境変数 ---
AZURE_ACCOUNT_NAME = env("AZURE_ACCOUNT_NAME", default=None)
AZURE_ACCOUNT_KEY = env("AZURE_ACCOUNT_KEY", default=None)
AZURE_CONTAINER_STATIC = env("AZURE_CONTAINER_STATIC", default=None)
AZURE_CONTAINER_MEDIA = env("AZURE_CONTAINER_MEDIA", default=None)

# --- 静的 / メディアの基本設定（ローカル用の出力先は常に設定） ---
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# --- Blob が利用可能なら Azure に切り替え、なければ WhiteNoise + FileSystem にフォールバック ---
if AZURE_ACCOUNT_NAME and AZURE_ACCOUNT_KEY and AZURE_CONTAINER_STATIC and AZURE_CONTAINER_MEDIA:
    # Azure Blob を使う設定
    STATIC_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER_STATIC}/"
    MEDIA_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER_MEDIA}/"

    STATICFILES_STORAGE = "mysite.storage_backends.AzureStaticStorage"
    DEFAULT_FILE_STORAGE = "mysite.storage_backends.AzureMediaStorage"

    # オブジェクトパラメータ（静的ファイル向けキャッシュ制御など）
    AZURE_OBJECT_PARAMETERS = {"cache_control": "public, max-age=31536000"}
else:
    # ローカル / 簡易本番用（WhiteNoise）設定
    STATIC_URL = "/static/"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

# --- セキュリティ関連（本番向けに環境変数で制御） ---
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=not DEBUG)
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=not DEBUG)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=not DEBUG)
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False)
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=False)
X_FRAME_OPTIONS = "DENY"

# --- ロギング（最小構成） ---
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# --- その他の便利設定 ---
# 管理画面の URL 等は必要に応じて変更
ADMIN_URL = env("ADMIN_URL", default="admin/")
