#!/bin/bash
# This script allow us to displays all HTTP methods the server will accept.
curl -X OPTIONS -i "$1"
