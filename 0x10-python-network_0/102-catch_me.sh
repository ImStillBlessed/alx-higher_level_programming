#!/bin/bash
# Send a PUT request to the specified URL with the user agent set to "You got me!"
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
