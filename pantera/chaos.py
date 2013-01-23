# Copyright 2013 Pantera authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import random
import re
import os

pid_regexp = re.compile(r"^\d+$")


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


class RemoteKill(object):
    name = "remote-kill"

    def __init__(self, process, host, user,
                 signal=9, priv_key=None, use_sudo=True):
        proc = str(process)
        self._process = proc
        self._cmd = pid_regexp.match(proc) is not None and "kill" or "killall"
        self._host = host
        self._user = user
        self._signal = signal
        self._key = priv_key is not None and "-i %s" % priv_key or ""
        self._sudo = use_sudo and "sudo" or ""

    def __call__(self):
        cmd = "ssh %(key)s -l %(user)s %(host)s " + \
              "%(sudo)s %(cmd)s -%(signal)d %(process)s"
        args = {
            "key": self._key,
            "user": self._user,
            "host": self._host,
            "sudo": self._sudo,
            "cmd": self._cmd,
            "signal": self._signal,
            "process": self._process,
        }
        cmd = (cmd % args).replace("  ", " ")
        os.system(cmd)
