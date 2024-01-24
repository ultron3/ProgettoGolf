#!/bin/bash

# Trova e termina il processo del server middleware
pid=$(ps aux | grep 'DbGolf.py' | grep -v grep | awk '{print $2}')

if [ -n "$pid" ]; then
    echo "Terminating middleware server..."
    kill -9 $pid
else
    echo "Middleware server is not running."
fi
