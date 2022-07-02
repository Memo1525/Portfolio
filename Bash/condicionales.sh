#!/bin/bash

response=$(curl --write-out "%{http_code}\n" --silent --output /dev/null "$1")

if [ $1 == https://google.com]; then
   echo "Siempre 200, no me tengo que fijar"

echo $1: $response 

#this bash script chech the status code returned by the we page so is veri useful for testing a lot of websites or in multiple pods or something
