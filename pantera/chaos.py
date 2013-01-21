# Copyright 2013 Pantera authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import random
import os


class EC2(object):

    def __init__(self, access, secret):
        self.access = access
        self.secret = secret

    def choice(self):
        """
        choose a vm
        """
        vms = self.conn.get_all_instances()
        vm = random.choice(vms)
        return vm.instances[0].id

    def connect(self):
        """
        creates an ec2 connection
        """
        from boto.ec2.connection import EC2Connection
        self.conn = EC2Connection(self.access, self.secret)


class Terminate(EC2):
    name = "terminate"

    def terminate(self):
        """
        terminates a vm
        """
        self.connect()
        vm = self.choice()
        return self.conn.terminate_instances(instance_ids=[vm])

    def __call__(self):
        self.terminate()


class Stop(EC2):
    name = "stop"

    def stop(self):
        """
        stops a vm
        """
        self.connect()
        vm = self.choice()
        return self.conn.stop_instances(instance_ids=[vm])

    def __call__(self):
        self.stop()


class Reboot(EC2):
    name = "reboot"

    def reboot(self):
        """
        reboots a vm
        """
        self.connect()
        vm = self.choice()
        return self.conn.reboot_instances(instance_ids=[vm])

    def __call__(self):
        self.reboot()


class Kill(object):
    name = "kill"

    def __init__(self, process, signal=9):
        self._process = process
        self._signal = signal

    def __call__(self):
        """
        Kills a process, sending the given signal.
        """
        os.kill(self._process, self._signal)
