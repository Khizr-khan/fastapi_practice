#!/usr/bin/env bash
host="$1"
port="$2"
timeout="$3"

for ((i=0; i<timeout; i++)); do
    nc -z "$host" "$port" && exit 0
    sleep 1
done

exit 1