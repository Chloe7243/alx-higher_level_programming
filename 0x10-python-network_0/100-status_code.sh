#!/bin/bash
# displays the body of the response if status is 200
curl -so /dev/null -w "%{http_code}" $1
