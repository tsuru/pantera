import unittest
import mock


class ChooseVmTestCase(unittest.TestCase):
    def test_choice_vm(self):
        instance = mock.Mock(id="1")
        reservation = mock.Mock(instances=[instance])
        with mock.patch("pantera.chaos.connect") as conn:
            with mock.patch("random.choice") as choice:
                from pantera import chaos
                choice.return_value = reservation
                vm = chaos.choice_vm(conn)
        self.assertEqual("1", vm)
