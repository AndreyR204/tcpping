#!/usr/bin/env python3
import sys
from tcping import app

host = None
port = 80

# Default to 10000 connections max
maxcount = 10000

# Host
try:
    host = sys.argv[1]
except IndexError:
    print("Usage: tcpping.py host [port] [maxCount]")
    sys.exit(1)

# Port
try:
    port = int(sys.argv[2])
except ValueError:
    print("Error: Port Must be Integer:", sys.argv[3])
    sys.exit(1)
except IndexError:
    pass

# maxCount
try:
    maxcount = int(sys.argv[3])
except ValueError:
    print("Error: Max Count Value Must be Integer", sys.argv[3])
    sys.exit(1)
except IndexError:
    pass
app.ping_hosts(host,port,maxcount)