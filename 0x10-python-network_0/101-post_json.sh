#!/bin/bash
# displays the body of the response if status is 200
curl -sXH "POST" "Content-Type: application/json" -d @$2 $1
