#!/bin/bash
# Sends a GET request with a specific header to the provided URL and displays the body
curl -sH "X-School-User-Id: 98" "$1"
