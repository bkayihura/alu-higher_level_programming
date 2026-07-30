#!/bin/bash
# Displays all HTTP methods the server accepts
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | cut -d " " -f 2-
