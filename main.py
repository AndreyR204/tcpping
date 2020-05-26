#!/usr/bin/env python3
import argparse
import sys
from tcping import app
from tcping import variables

parser = argparse.ArgumentParser()
parser.add_argument('--host', '-H', default='127.0.0.1', help='host')
parser.add_argument('--port', '-p', default=80, help='port')
parser.add_argument('--max', '-m', default=100, help='max count')
args = parser.parse_args()
# Host
try:
    host = args.host
except IndexError:
    print("Usage: tcpping.py host [port] [maxCount]")
    sys.exit(1)

# Port
try:
    port = args.port
except ValueError:
    print("Error: Port Must be Integer:", args.port)
    sys.exit(1)
except IndexError:
    pass

# maxCount
try:
    maxcount = int(args.max)
except ValueError:
    print("Error: Max Count Value Must be Integer", args.max)
    sys.exit(1)
except IndexError:
    pass
app.ping_hosts(args.host, args.port, args.max)
app.get_results(variables.count, variables.passed, variables.failed)