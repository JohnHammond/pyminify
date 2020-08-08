#!/usr/bin/env python3

import argparse
import os
import sys

# Ensure that this includes an argument for the file
parser = argparse.ArgumentParser()
parser.add_argument("script", type=str)
args = parser.parse_args()

if not os.path.exists(args.script):
	sys.stderr.write(f"'{args.script}' not a file")

with open(args.script, "rb") as h:
	contents = h.read().decode('utf-8')

code_string = "+".join([f"chr({ord(x)})" for x in contents])
code_string = f"{code_string}"

script_string = "+".join([f"chr({ord(x)})" for x in "<script>"])
script_string = f"{script_string}"

exec_string = "+".join([f"chr({ord(x)})" for x in "exec"])
exec_string = f"{exec_string}"

print(f'python -c "exec(compile({code_string}, {script_string}, {exec_string}))"')