#!/bin/bash
# Sends a POST request with specific parameters to the provided URL and displays the body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
