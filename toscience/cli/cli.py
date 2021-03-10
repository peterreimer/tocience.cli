#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import requests
import urllib.parse
import logging
import os
import sys
import pkg_resources
import toscience.config


apiurl = toscience.config.apiurl
namespace = toscience.config.namespace
user = toscience.config.user
password = toscience.config.password
datadir = toscience.config.datadir
collectionUrl = toscience.config.collectionUrl


version = pkg_resources.require("toscience.cli")[0].version
logger = logging.getLogger(__name__)
DEFAULT_LOGFILE = "toscience.log"

class Client:

    def __init__(self, endpoint):

        self.endpoint = endpoint
        self.path = "resource"

    def _make_rest_uri(self, parentPID, query=""):
        """create the uri for the restfull webservice of orcid"""
        
        path = "/".join((self.path, parentPID, "postResearchData"))
        if not self.endpoint:
            logger.error('No valid endpoint specified.')
            rest_uri = None
        else:
            rest_uri = urllib.parse.urlunparse(('https', apiurl, path, '', query, ''))
        logger.info("REST URI %s" % rest_uri)
        return rest_uri
 

    def add(self, parentPID, subPath, filename, resourcePid=""):

        qdict = {
            'collectionUrl':'data',
            'subPath': subPath,
            'filename': filename,
            'resourcePid': resourcePid
            } 
        query = urllib.parse.urlencode(qdict)
        headers = {
            "UserId": "resourceposter",
            "Content-Type": "text/plain; charset=utf-8"
            }
        auth = (user, password)

        url = self._make_rest_uri(query=query, parentPID= parentPID)
        print (url)
        response = requests.post(url, auth=auth, headers=headers)
        print(response)
        if (response.status_code != 200):
            return str(response.status_code) + " " + response.text
        else:
            return response.text


def scan(parentPID, depth):
    """ Return (subdir, filename) Tupels für all files in given directory

    Makes currently only sense for depth=1, since the endpoint does not support
    more.
    """
    resource_dir = os.path.join(datadir, parentPID)
    resources = []
    toplevel = resource_dir.count(os.path.sep)
    for root, directories, files in os.walk(resource_dir, topdown=True):
        level = root.count(os.path.sep) - toplevel
        subdir = os.path.split(root)[-1]
        if level <= depth:
            for file in files:
                resources.append((subdir, file))
      
    return resources






def main():

    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logger.addHandler(console)


    parser = argparse.ArgumentParser(description='to science command line interface')
    parser.add_argument('-l', '--logfile', default="DEFAULT_LOGFILE", help='Name of the logfile (default: %s)' % DEFAULT_LOGFILE)
    parser.add_argument('-v', '--version', action='store_true', help='Print version number and exit')
    subparsers = parser.add_subparsers(help='available sub-commands')
    # create the parser for the "ingest" command
    parser_ingest = subparsers.add_parser('ingest', help='Batch ingesting a directory')
    parser_ingest.add_argument('pid', help="PID")

    # create the parser for the "user" command
    parser_ingest = subparsers.add_parser('user', help='Manage api users (not yet implemented)')
    
  
    args = parser.parse_args()
    logfile = args.logfile
    if args.version:
        print("toscience.cli version %s" % version)
        sys.exit(0)
    print(args) 



if __name__ == '__main__':

    parentPID = "frl:6402662"
    client = Client("postResearchData")
    for subdir, filename in scan(parentPID, 1):
        print(subdir, filename)
        client.add(parentPID, subdir, filename)

    
    
