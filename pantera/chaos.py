import random


def connect(access, secret):
    """
    creates an ec2 connection
    """
    from boto.ec2.connection import EC2Connection
    return EC2Connection(access, secret)


def destroy_vm(access, secret):
    """
    destroy a vm
    """
    conn = connect(access, secret)
    vm = choice_vm(conn)
    return conn.terminate_instances(instance_ids=[vm])


def choice_vm(conn):
    """
    choice a vm
    """
    vms = conn.get_all_instances()
    vm = random.choice(vms)
    return vm.instances[0].id
