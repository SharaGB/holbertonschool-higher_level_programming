#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | sed -n 's/Allow: //p'
