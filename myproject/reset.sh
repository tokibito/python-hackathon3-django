#!/bin/bash
dbfile=myproject.db

if [ -f $dbfile ]
then
  rm $dbfile
fi

python manage.py syncdb --noinput
python manage.py loaddata test
