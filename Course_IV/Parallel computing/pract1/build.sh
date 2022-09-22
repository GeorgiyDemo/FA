#!/bin/bash
g++ -Xpreprocessor -fopenmp  -I/opt/homebrew/Cellar/libomp/14.0.6/include -L/usr/local/lib -lomp $1  -o out.a
./out.a