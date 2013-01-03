import random


class Terminate(object):
    def __init__(self, access, secret):
        self.access = access
        self.secret = secret

    def choice(self):
        """
        choice a vm
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

    def terminate(self):
        """
        terminates a vm
        """
        self.connect()
        vm = self.choice()
        return self.conn.terminate_instances(instance_ids=[vm])

    def execute(self):
        self.terminate()


class Stop(object):
    def __init__(self, access, secret):
        self.access = access
        self.secret = secret

    def choice(self):
        """
        choice a vm
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

    def stop(self):
        """
        stops a vm
        """
        self.connect()
        vm = self.choice()
        return self.conn.stop_instances(instance_ids=[vm])

    def execute(self):
        self.stop()
