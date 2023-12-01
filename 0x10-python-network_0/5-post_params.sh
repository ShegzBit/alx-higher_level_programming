#!/bin/bash
# a script that makes a post request
curl -sF "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
