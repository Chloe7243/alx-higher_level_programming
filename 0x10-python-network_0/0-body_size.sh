#!/bin/bash
# displays the size of the body of the response
curl -sw "\n%{size_download}\n" $1 | tail -n1
