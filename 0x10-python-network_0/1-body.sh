#!/bin/bash
# displays the body of the response if status is 200
[[ $(curl -sLw "\n%{http_code}\n" $1 | tail -n1) -eq 200 ]] && curl -sL $1
