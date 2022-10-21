#!/bin/bash
# display number of bytes in location
curl -sI $1 | wc -c
