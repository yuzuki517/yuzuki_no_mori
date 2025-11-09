#!/bin/bash
set -e

# マイグレーション（起動時に DB スキーマを最新にする）
python manage.py migrate --noinput

# collectstatic（念のため起動時にも実行）
python manage.py collectstatic --noinput

# Gunicorn でアプリを起動
# Azure App Service では $PORT が割り当てられるためそれを使う
: "${PORT:=8000}"
exec gunicorn --bind 0.0.0.0:${PORT} mysite.wsgi:application
