#!/usr/bin/env bash
# This script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

URL=$1
SIZE=$(curl -sI "$URL" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n')
echo "$SIZE"
