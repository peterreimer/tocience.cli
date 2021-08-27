#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import json
import bitmath

def get_sizes(root_dir):

    sizes = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            rel_dir = os.path.relpath(root, root_dir)
            rel_file = os.path.join(rel_dir, file)
            abs_file = os.path.join(root, file)
            bytes = os.path.getsize(abs_file)
            size = bitmath.Byte(bytes).best_prefix(system=bitmath.SI)
            #print(s)
            #size = bitmath.getsize(abs_file, system=bitmath.SI)
            sizes[rel_file] = {'bytes': bytes, 'human':size.format("{value:.1f}{unit}")}

    return json.dumps(sizes, indent=4)

def main():

    parser = argparse.ArgumentParser(description='Create a json file with filesizes')
    parser.add_argument('directory', help='Directory')

    args = parser.parse_args()

    if os.path.isdir(args.directory):
        print(get_sizes(args.directory))
    else:
        print("%s is not a directory" % args.directory)
        sys.exit(0)
