toscience.cli
=============

Ingest the content of a directory (one level) as unmanaged content into  fedora via the to.science.api.

Installation for production:
---------------------------

.. code-block:: bash
    
    $ mkdir /opt/toscience.cli
    $ cd /opt/toscience.cli
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install https://dist.pubsys.hbz-nrw.de/toscience.cli-0.1.tar.gz


Installation for development:
-----------------------------

.. code-block:: bash
    
    $ cd mkdir /opt
    $ git clone git@github.com:peterreimer/toscience.cli.git
    $ cd /opt/toscience.cli
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install -e .

Usage
-----

.. code-block:: bash

    $ toscience -h
    usage: toscience [-h] [-l LOGFILE] [-v] {ingest,user} ...

    to science command line interface

    positional arguments:
    {ingest,user}         available sub-commands
        ingest              Batch ingesting a directory
        user                Manage api users (not yet implemented)

    optional arguments:
    -h, --help            show this help message and exit
    -l LOGFILE, --logfile LOGFILE
                            Name of the logfile (default: toscience.log)
    -v, --version         Print version number and exit
