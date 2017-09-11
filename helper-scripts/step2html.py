#! /usr/bin/env python3
from sys import argv
if len(argv) != 2 or argv[1].strip() in {'-h','--help'}:
    print("USAGE: python step2html.py <step_file>")
    exit(-1)
null = None; true = True; false = False
print(eval(open(argv[1]).read())['block']['text'])
