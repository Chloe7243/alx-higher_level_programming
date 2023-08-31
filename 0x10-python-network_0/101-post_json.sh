#!/bin/bash
# displays the body of the response if status is 200
curl -sX "POST" -H "Content-Type: application/json" -d @$2 $1
