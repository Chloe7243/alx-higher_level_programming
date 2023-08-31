#!/bin/bash
# displays the size of the body of the response
curl -sw "%{size_request}\n" $1 | tail -n1
