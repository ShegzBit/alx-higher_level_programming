#!/bin/bash
# a script that prints all allowed methods on a url
curl -sI ALLOW "$1" | grep "Allow" | awk -F': ' '{print $2}'
