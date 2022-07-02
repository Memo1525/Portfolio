#!/bin/bash

for i in 1 2 3 4 5
do 
   echo "Hello $i"
done

for i in $(ls)
do
   echo "Hola $1"
done

for (( c==1; c<=5; c++ )) #here we are using sintax of c 
do
   echo "Hola $c"
done
