#!/bin/bash
# This script sends a header variable.
curl -s -X GET -H "X-School-User-Id: 98" "$1"
