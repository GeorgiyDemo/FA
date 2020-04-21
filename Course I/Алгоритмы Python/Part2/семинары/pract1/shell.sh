#!/bin/bash
for i in {1..10000}
do
  echo "*Итерация №$i* "  
  python3 final.py
  sleep 1
done