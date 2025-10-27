#!/bin/bash
gunicorn mysite.wsgi --bind=0.0.0.0 --timeout 600

