#!/bin/bash
# displays the size of the body of the response
curl -sw "%{size_request}\n" $1 | grep -o -E '[0-9]+'
