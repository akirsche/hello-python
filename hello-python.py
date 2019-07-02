#!/usr/bin/env python3

import sys

name=sys.argv[1] if len(sys.argv) > 1 else '--'
print("Hello {who}".format(who=name)) 