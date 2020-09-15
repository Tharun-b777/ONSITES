#!/bin/bash
time=$(date +"%M")
minute=$((time+1))
while true
do
time=$(date +"%M")
if [ $time -eq $minute ]
then
minute=$((time+1))
git commit -m"testing"
fi
done