#!/bin/bash

# to run this file need to use ./runserver.sh as this executable is not in the path

# cd '/Users/pinchy/Documents/GitHub/L3T10'
source my_django/bin/activate
cd bandPage
python3 manage.py runserver
