#!/bin/sh

# 오류가 나면 알려줘
set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

# uWSGI: 유저가 보낸 데이터를 Nginx가 받아와서 => uWSGI로 전달 => uWSGI가 Django로 전달
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi

