#!/bin/bash
read -p "Enter text" txt  
echo "$txt" > tmp
read -p "Enter your image extension " ext
steghide embed -ef tmp -cf *.${ext}
rm tmp 
read -p "Do you want to read text(y/n)??" reply 
case $reply in 
y)
steghide extract -sf *.jpg 
cat tmp 
rm tmp ;;

*)
exit 0;;

esac
