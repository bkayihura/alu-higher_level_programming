#!/bin/bash
# Sends a JSON POST request using the contents of a file and displays the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
