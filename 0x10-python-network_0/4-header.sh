#!/bin/bash
# a script that shares passes a header with a get request
curl -siH "X-School-User-Id: 98" "$1"
