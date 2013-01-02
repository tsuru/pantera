import unittest
import mock



class RemoveVmTestCase(unittest.TestCase):
    def test_remove_vm(self):
        vms = ["1", "2"]
        with mock.patch("boto.ec2.connection.EC2Connection") as ec2con:
            from pantera import caos
            conn= ec2con.return_value
            conn.terminate_instances.return_value = vms
            destroyed = caos.destroy_vm()
        self.assertListEqual(vms, destroyed)
