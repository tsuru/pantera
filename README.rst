.. image:: https://secure.travis-ci.org/tsuru/pantera.png
   :target: http://travis-ci.org/tsuru/pantera

.. image:: https://pypip.in/version/pantera/badge.svg
    :target: https://pypi.python.org/pypi/pantera/
    :alt: Latest Version

pantera
=======

Pantera is a tool to test the resilience of cloud applications. It's based on
EC2 instances, and process management. It's able to destroy, stop and reboot
instances, and also able to kill process locally and remotely.

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

.. code-block:: pycon

    >>> from pantera import random_run
    >>> random_run("ec2-access-key", "ec2-secret-key")

This will run a random action, using the given parameters.

You can also run a specific action:

.. code-block:: pycon

    >>> from pantera import run
    >>> run("terminate", "ec2-access-key", "ec2-secret-key")

To check the list of available actions:

.. code-block:: pycon

    >>> from pantera import list_actions
    >>> list_actions()
