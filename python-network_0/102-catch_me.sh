#!/bin/bash
# Makes a request that causes the server to say "You got me!"
curl -s -X GET -H "You-Get-Me: 98" 0.0.0.0:5000/catch_me
