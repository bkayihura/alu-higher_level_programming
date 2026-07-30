#!/bin/bash
# Displays only the status code of the response, following redirects
curl -s -o /dev/null -w "%{http_code}" -L "$1"
