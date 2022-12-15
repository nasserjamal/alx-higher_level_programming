#!/usr/bin/env bash
curl -I $1 | grep Content-Length: | cut -d: -f2-
