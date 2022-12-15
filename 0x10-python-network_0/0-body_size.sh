#!/usr/bin/env bash
# Prints the content length
curl -sI $1 | grep Content-Length: | cut -d " " -f2-
