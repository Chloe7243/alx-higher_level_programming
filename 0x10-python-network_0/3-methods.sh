#!/bin/bash
# displays the body of the response if status is 200
curl -sI $1 | grep "Allow" | cut -c 8-
