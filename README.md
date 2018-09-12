==============
ICOFUNDER.IO
==============

example website

### Install
apt-get install python-pip mysql-server git nginx libmysqlclient-dev python-dev supervisor gettext python-scrypt python-qrcode libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
git clone git@bitbucket.org:wahahahappy/icofunder.git

pip install -r requirements.txt


mysql -uroot -p
create database icofunder default character set utf8;

python manage.py migrate
python manage.py runserver



### Django and Javascript i18n

python manage.py makemessages
python manage.py makemessages -d djangojs
python manage.py compilemessages


mkdir /var/log/nginx/ico /var/log/ico
