import unittest
import mock


class RemoveVmTestCase(unittest.TestCase):
    def test_remove_vm(self):
        vms = ["1"]
        with mock.patch("pantera.chaos.connect") as conn:
            with mock.patch("pantera.chaos.choice_vm") as choice:
                choice.return_value = "1"
                instance = mock.Mock()
                instance.terminate_instances.return_value = vms
                conn.return_value = instance
                from pantera import chaos
                destroyed = chaos.destroy_vm("access", "secret")
        self.assertListEqual(vms, destroyed)
