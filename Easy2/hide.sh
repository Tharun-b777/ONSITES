#!/bin/bash
read -p "Enter text" txt  
echo "$txt" > tmp
steghide embed -ef tmp -cf *.jpg
rm tmp 
read -p "Do you want to read text(y/n)??" reply 
case $reply in 
y)
steghide extract -sf *.jpg 
cat tmp 
rm tmp ;;

*)
exit;;

esac
