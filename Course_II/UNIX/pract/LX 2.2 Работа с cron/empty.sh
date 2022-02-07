#!/bin/bash
echo "Working"
DATE=$(date '+%H-%M-%S')
TIME=$(date +"%T")
echo $TIME > tmp/$DATE.txt
echo $DATE
