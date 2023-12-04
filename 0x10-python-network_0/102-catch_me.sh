#!/bin/bash
# a script that tries to catch the url
curl -sLX PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
