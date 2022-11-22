#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""usage: blobtools nodesdb             --nodes <NODES> --names <NAMES>   --nodesDB <DB>
                                        [-h|--help]

    Options:
        -h --help                       show this
        --nodes <NODES>                 NCBI nodes.dmp file.
        --names <NAMES>                 NCBI names.dmp file.
        --nodesDB <DB>                  NCBI db file.
 
"""

from __future__ import division
from docopt import docopt

from os.path import join, dirname, abspath

import lib.BtIO as BtIO

def main():
    args = docopt(__doc__)
    names_f = args['--names']
    nodes_f = args['--nodes']
    nodesDB_f = args['--nodesDB']  # added

    # Parse names.dmp, nodes.dmp
    nodesDB_default = join(dirname(abspath(__file__)), "../data/nodesDB.txt")
    
    if nodesDB_f:
       nodesDB, nodesDB_f = BtIO.parseNodesDB(nodes=nodes_f, names=names_f, nodesDB=nodesDB_f, nodesDBdefault=nodesDB_default)
    else:    
       nodesDB, nodesDB_f = BtIO.parseNodesDB(nodes=nodes_f, names=names_f, nodesDB=None, nodesDBdefault=nodesDB_default)

if __name__ == '__main__':
    main()
