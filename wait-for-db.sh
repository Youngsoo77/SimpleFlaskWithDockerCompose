#!/bin/bash
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

until mysql -h $DBADDR -u $DBUSER -p$DBPASS -c '\q'; do
  >&2 echo "DB is unavailable - sleeping"
  sleep 5
done

>&2 echo "DB is up - executing command"

exec $cmd