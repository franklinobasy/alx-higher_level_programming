#!/bin/bash
# display number of bytes in location
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
