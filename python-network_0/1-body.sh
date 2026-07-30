#!/bin/bash
# Displays the body of the response only if status code is 200
curl -s -o /tmp/body_output -w "%{http_code}" -L "$1" | grep -q "^200$" && cat /tmp/body_output
