#!/bin/bash
# a script that posts json
curl -sH "Content-Type: application/json" -d "@$2" "$1"
