#!/bin/bash
find $HOME/tmp/. -mmin -17 -type f -exec rm -rf {} \;
echo "Removed files"
