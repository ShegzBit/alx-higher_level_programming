#!/bin/bash
# a script that prints the content length of the response
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
