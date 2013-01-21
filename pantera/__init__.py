# Copyright 2013 Pantera authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import chaos
import random


__version__ = "0.1.1"


def run(*args, **kwargs):
    run_list = [chaos.Stop, chaos.Reboot, chaos.Terminate]
    random.choice(run_list)(*args, **kwargs)()
