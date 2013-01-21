# Copyright 2013 Pantera authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import chaos
import random


__version__ = "0.1.1"

_actions = {
    chaos.Stop.name: chaos.Stop,
    chaos.Reboot.name: chaos.Reboot,
    chaos.Terminate.name: chaos.Terminate,
    chaos.Kill.name: chaos.Kill,
}


def run(name, *args, **kwargs):
    _actions[name](*args, **kwargs)()


def random_run(*args, **kwargs):
    action = random.choice(_actions.keys())
    run(action, *args, **kwargs)
