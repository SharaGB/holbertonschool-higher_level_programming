#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
# URL="$1"
curl -sI $1 | grep -i Content-Length | cut -d' ' -f2 # awk '{print $2}' works too!, but it's slower than cut
