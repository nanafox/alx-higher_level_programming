#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me_3 that causes the server to respond with a message containing You got me!
curl -sL 0.0.0.0:5000/catch_me_2 -H "Origin: School" -X PUT -d "user_id=98"
