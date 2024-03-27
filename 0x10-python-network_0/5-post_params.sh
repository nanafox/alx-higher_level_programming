#!/bin/bash
# This script sends a POST request (with data) to the passed URL, and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
