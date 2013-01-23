.. image:: https://secure.travis-ci.org/globocom/pantera.png
   :target: http://travis-ci.org/globocom/pantera

pantera
=======

pantera is a tool to test the resilience fo cloud applications based on ec2.

Installation
------------

::

    $ pip install pantera

Usage
-----

First open the interactive python shell:

::

    $ python

Then:

::

    >>> from pantera import random_run
    >>> random_run("ec2-access-key", "ec2-secret-key")

This will run a random action, using the given parameters.

You can also run a specific action:

::

    >>> from pantera import run
    >>> run("terminate", "ec2-access-key", "ec2-secret-key")

To check the list of available actions:

::

    >>> from pantera import list_actions
    >>> list_actions()
