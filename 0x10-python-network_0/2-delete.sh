#!/bin/bash
# Sends a delete request to the address passed as an argument
curl -s "$1" -X DELETE
