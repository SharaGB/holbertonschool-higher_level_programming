#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -so /dev/null -I -w "%{http_code}" "$1" # -I: added to improve response load performance
