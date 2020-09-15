#!/bin/bash 
LIMIT=500
j=2
while true
do 
ID=$(ps -o pid ax)
for i in $ID 
do 
if [ "$i" = "PID" ]
then 
continue
fi
a=$(pmap $i | grep total | grep -o "[0-9]*K" | grep -o "[0-9]*") 
a=$((a/1024))
if [ $a -gt $LIMIT ]
then
kill -9 $i
fi
done 
done
