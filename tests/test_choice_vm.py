import unittest
import mock


class ChooseVmTestCase(unittest.TestCase):
    def test_choice_vm(self):
        vms = ["1", "2"]
        expected = "1"
        with mock.patch("boto.ec2.connection.EC2Connection") as ec2con:
            conn = ec2con.return_value
            conn.terminate_instances.return_value = vms
            with mock.patch("random.choice") as choice:
                from pantera import caos
                choice.return_value = expected
                vm = caos.choice_vm()
        self.assertEqual(expected, vm)
