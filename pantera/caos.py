from boto.ec2.connection import EC2Connection


def destroy_vm():
    """
    destroy_vm destroy a vm
    """
    conn = EC2Connection("accss", "secret")
    return conn.terminate_instances(instance_ids=[])
