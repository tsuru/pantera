#pantera

pantera is a tool to test the resilience fo cloud applications based on ec2.

##Installation

    $ pip install pantera

##Usage

First open the interactive python shell:

    $ python

Then:

    >>> from pantera import run
    >>> run("ec2-access-key", "ec2-secret-key")

