#!/bin/bash
# This script allow us to displays all HTTP methods the server will accept.
curl -I -X HEAD -s http://www.example.com | grep -i allow | awk '{print $2}'
