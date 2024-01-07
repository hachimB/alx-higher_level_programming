#!/bin/bash
# This script sends a header variable.
curl -s -o /dev/null -w "%{http_code}" -X GET -H "X-School-User-Id: 98" "$1"
