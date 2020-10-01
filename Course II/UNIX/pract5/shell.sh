#!/bin/bash
sudo useradd "user$1"
yes "pass$1" | sudo passwd "user$1"
