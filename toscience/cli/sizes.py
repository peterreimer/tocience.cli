#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import json


def get_sizes(path):

    sizes = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            #list_of_files.append((path, size))
            sizes[path] = size

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




