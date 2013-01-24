# Copyright 2013 Pantera authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import chaos
import random

__version__ = "0.2"

_actions = {
    chaos.Stop.name: chaos.Stop,
    chaos.Reboot.name: chaos.Reboot,
    chaos.Terminate.name: chaos.Terminate,
    chaos.Kill.name: chaos.Kill,
    chaos.RemoteKill.name: chaos.RemoteKill,
    chaos.UpstartStop.name: chaos.UpstartStop,
}


def list_actions():
    return _actions


def run(name, *args, **kwargs):
    a = _actions.get(name)
    if a is None:
        raise UnknownAction(name)
    a(*args, **kwargs)()


def random_run(*args, **kwargs):
    action = random.choice(_actions.keys())
    run(action, *args, **kwargs)


class UnknownAction(Exception):

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return "Unknown action: %s." % self._name

    def __unicode__(self):
        return unicode(self.__str__())
