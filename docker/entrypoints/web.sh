#!/bin/bash

# A reference entrypoint for running a django gunicorn webserver.

export DBUSER=postgres
export DBNAME=jenkins-test
export DBHOST=$POSTGRES_PORT_5432_TCP_ADDR
export DBPORT=$POSTGRES_PORT_5432_TCP_PORT

# Check that the database does not exist.
if ! psql -lqt -h $DBHOST -p $DBPORT -U $DBUSER | cut -d \| -f 1 | grep -w $DBNAME; then
    echo "Creating database..."
    createdb -h $DBHOST -p $DBPORT -U $DBUSER $DBNAME
    echo "Done!"
fi


cd $APP_DIR/$APP_NAME

# 1. Put the database on a consistent state.
python manage.py syncdb --noinput
python manage.py migrate --noinput

# 2. Add any other build step, like building your css or js files.
python manage.py collectstatic --noinput

# 3. Run your webserver of choice
gunicorn --workers 2 -b 0.0.0.0:80 wsgi
