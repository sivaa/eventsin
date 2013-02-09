mysql -u root -proot -e "drop schema eventsin; create schema eventsin;"
python manage.py syncdb
