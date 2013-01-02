from boto.ec2.connection import EC2Connection

import random


def destroy_vm():
    """
    destroy a vm
    """
    conn = EC2Connection("accss", "secret")
    return conn.terminate_instances(instance_ids=[])


def choice_vm():
    """
    choice a vm
    """
    conn = EC2Connection("accss", "secret")
    vms = conn.get_all_instances()
    return random.choice(vms)
