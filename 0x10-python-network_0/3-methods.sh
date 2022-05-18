#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep 'Allow:' | sed -n 's/Allow: //p'
