#!/bin/bash
set -e

SERVER="dev-postgres";
PW="Rm345.ho";
DB="bluumdb";


echo "echo stop & remove old docker [$SERVER] and starting new fresh instance of [$SERVER]"
(docker kill $SERVER || :) && \
  (docker rm $SERVER || :) && \
  docker run --name $SERVER -e POSTGRES_PASSWORD=$PW \
  -e PGPASSWORD=$PW \
  -p 5432:5432 \
  -d postgres

# wait for pg to start
echo "sleep wait for pg-server [$SERVER] to start";
SLEEP 3;
SLEEP 20;

#create the db 
echo "CREATE DATABASE $DB ENCODING 'UTF-8';" | docker exec -i $SERVER psql -U postgres
echo "\l" | docker exec -i $SERVER psql -U postgres

SLEEP 3;
#creating the dump
 
SLEEP 35;
#pg_dump -h intento5.cnx1lebkbeef.us-east-1.rds.amazonaws.com -p 5432 -U postgres -f  dump2.sql intento5