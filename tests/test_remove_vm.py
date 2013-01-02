import unittest
import mock


class RemoveVmTestCase(unittest.TestCase):
    def test_remove_vm(self):
        vms = ["1", "2"]
        with mock.patch("pantera.chaos.connect") as conn:
            instance = mock.Mock()
            instance.terminate_instances.return_value = vms
            conn.return_value = instance
            from pantera import chaos
            destroyed = chaos.destroy_vm("access", "secret")
        self.assertListEqual(vms, destroyed)
