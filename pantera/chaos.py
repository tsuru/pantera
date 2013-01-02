import random


def connect(access, secret):
    """
    creates an ec2 connection
    """
    from boto.ec2.connection import EC2Connection
    return EC2Connection(access, secret)


def destroy_vm():
    """
    destroy a vm
    """
    conn = connect("access", "secret")
    return conn.terminate_instances(instance_ids=[])


def choice_vm():
    """
    choice a vm
    """
    conn = connect("access", "secret")
    vms = conn.get_all_instances()
    return random.choice(vms)
