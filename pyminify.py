#!/usr/bin/env python3

import argparse
import os
import sys

def encode_string_with_chr(data: str) -> str:
	return "+".join([f"chr({ord(x)})" for x in data])

def encode_string(data: str, using_map: bool) -> str:
	if not using_map:
		return encode_string_with_chr(data)

	utf8_string = encode_string_with_chr('utf-8')
	encoded_string = '[' + ','.join(map(lambda x: str(ord(x)),data)) + ']'
	return f"str(bytes({encoded_string}),{utf8_string})"

# Ensure that this includes an argument for the file
parser = argparse.ArgumentParser()
parser.add_argument('--use-map', action='store_true')
parser.add_argument("script", type=str)
args = parser.parse_args()

if not os.path.exists(args.script):
	sys.stderr.write(f"'{args.script}' not a file")

with open(args.script, "rb") as h:
	contents = h.read().decode('utf-8')

code_string = encode_string(contents, args.use_map)
script_string = encode_string("<script>", args.use_map)
exec_string = encode_string("exec", args.use_map)

print(f'python -c "exec(compile({code_string},{script_string},{exec_string}))"')
