#!/bin/bash
# This script allow us to displays all HTTP methods the server will accept.
curl -s -X OPTIONS "$1"